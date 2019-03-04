"""The Python implementation of a GRPC chat server."""

from concurrent import futures
from collections import deque
import time
import yaml
import grpc

import chat_pb2
import chat_pb2_grpc
from chatlog import *

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
CONFIG_FILE = "config.yaml"
SERVER_PORT = '50051'
LRU_SIZE = 100

# includes all 1-1 chats + groups chats
chats = dict()

# list of groups a user is a member of
# returned as part of login request
usergroups = dict()


class Msg():
    def __init__(self, s=None, r=None, m=None, i=0):
        self.s = s
        self.r = r
        self.m = m
        self.i = i


class Chat():
    def __init__(self):
        self.chatid = None
        self.members = []
        self.isgroup = False
        self.messages = deque([], maxlen=LRU_SIZE)
        self.lastmsgid = 0

    def __init__(self, chatid, members, isgroup):
        self.chatid = chatid
        self.members = members
        self.isgroup = isgroup
        self.messages = deque([], maxlen=LRU_SIZE)
        self.lastmsgid = 0

    def GetChatId(self):
        return self.chatid

    def GetMembers(self):
        return self.members


def _CreatePseudoGroupName(user1, user2):
    _list = [user1, user2]
    _list.sort()
    return ":".join(_list)


def ParseConfig(configFilePath):
    global usergroups
    with open (configFilePath, "r") as confFile:
        config = yaml.load(confFile)
    LOG(LOG_DEBUG, "Loaded config: {}".format(config))
    users = config.get('users', [])
    for user1 in users:
        _user1groups = chat_pb2.Groups()
        for user2 in users:
            if user1 == user2:
                continue
            _pseudoname = _CreatePseudoGroupName(user1, user2)
            _members = [user1, user2]
            _isgroup = False
            _currChat = Chat(chatid=_pseudoname, members=_members, isgroup=_isgroup)
            chats[_pseudoname] = _currChat
            _group = _user1groups.groups.add()
            _group.groupid = _pseudoname
            _group.isgroup = False
            curruser = _group.users.add()
            curruser.name = user1
            otheruser = _group.users.add()
            otheruser.name = user2
        usergroups[user1] = _user1groups

    _groups = config.get('groups', [])
    for _groupname, _members in _groups.items():
        _currGroup = Chat(chatid=_groupname, members=_members, isgroup=True)
        chats[_groupname] = _currGroup
        for _member1 in _members:
            _user1groups = usergroups.get(_member1, chat_pb2.Groups())
            _group = _user1groups.groups.add()
            _group.groupid = _groupname
            _group.isgroup = True
            curruser = _group.users.add()
            curruser.name = _member1
            for _member2 in _members:
                if _member1 == _member2:
                    continue
                otheruser = _group.users.add()
                otheruser.name = _member2
            if _member1 not in usergroups:
                usergroups[_member1] = _user1groups

    LOG(LOG_DEBUG, "Setup chats: {}".format(chats))
    LOG(LOG_DEBUG, "Setup usergroups: {}".format(usergroups))


def StoreMsg(groupid, msg):
    chat = chats.get(groupid, None)
    LOG(LOG_DEBUG, "In StoreMsg Chat is : {}".format(chat))
    if chat is None:
        return None
    assert(msg.s in chat.members)

    try:
        _msgid = chat.lastmsgid + 1
        msg.i = _msgid
        chat.messages.append(msg)
        chat.lastmsgid = _msgid
        LOG(LOG_DEBUG, "Msg#{} queued for {}".format(_msgid, groupid))
        return _msgid
    except Exception as e:
        LOG(LOG_ERR, "Failed to store message {}: {}".format(msg, e))
        return None


def RetrieveMsgsFromChat(chatid, requester=None, marker=None):
    chat = chats.get(chatid, None)
    if chat is None:
        LOG(LOG_ERR, "Chat {} not found".format(chatid))
        return None
    msg = None
    msgs = chat.messages
    try:
        msg = msgs.popleft()
    except IndexError:
        LOG(LOG_DEBUG, "No more messages for {}".format(chatid))
    except Exception as e:
        LOG(LOG_ERR, "Exception {} while retrieving messages for {}: {}".format(chatid, e))
    return msg


def GetChatsForUser(user):
    return usergroups.get(user, None)


class Messenger(chat_pb2_grpc.SpartanMessengerServicer):
    def LoginUser(self, req, ctx):
        chatlist = None
        LOG(LOG_DEBUG, "Login request for {}".format(req.name))
        try:
            username = req.name
            chatlist = GetChatsForUser(username)
        except Exception as e:
            LOG(LOG_ERR, "Failed to login {}: {}".format(req.name, e))
        finally:
            if chatlist:
                return chatlist
            else:
                return chat_pb2.Groups(groups=[])

    def ReceiveMessage(self, req, ctx):
        _userlastmsgid = req.msgid
        try:
            _currmsgid = None
            if req.recipient and req.msg:
                _msg = Msg(s=req.sender, r=req.recipient, m=req.msg)
                _currmsgid = StoreMsg(groupid=req.recipient, msg=_msg)
            groupid = req.recipient
            chat = chats.get(groupid, None)

            if chat is None:
                yield chat_pb2.Message(sender=None, recipient=groupid, msg=None, msgid=None)
                return
            msgs = chat.messages
            _chatlastid = chat.lastmsgid
            if len(msgs) == 0:
                yield chat_pb2.Message(sender=None, recipient=groupid, msg=None, msgid=_chatlastid)
                return
            else:
                for msg in msgs:
                    if msg.i > _userlastmsgid and msg.i != _currmsgid:
                        yield chat_pb2.Message(sender=msg.s, recipient=msg.r, msg=msg.m, msgid=msg.i)

            yield chat_pb2.Message(sender=None, recipient=groupid, msg=None, msgid=_chatlastid)
            return
        except Exception as e:
            LOG(LOG_ERR, "Failed to receive message for {}: {}".format(req.sender, e))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_SpartanMessengerServicer_to_server(Messenger(), server)
    server.add_insecure_port('[::]:{}'.format(SERVER_PORT))
    server.start()
    print("Spartan server started on port {}.".format(SERVER_PORT))
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    ParseConfig(CONFIG_FILE)
    serve()
