"""The Python implementation of a GRPC chat client."""

from __future__ import print_function

import grpc
import sys
from spartan_crypto import *
import chat_pb2
import chat_pb2_grpc
from chatlog import *

SERVER_HOST = 'localhost'
SERVER_PORT = 50051
SERVER_ADDR = "{}:{}".format(SERVER_HOST, SERVER_PORT)

# Current user name
user = ""
# Available chats for this user
clientchats = dict()
# List of chats for printing menu to send message
userlist = ""


def Usage(progName):
    print("Usage: {} <name>".format(progName))


def _spartanPrint(string):
    print("[Spartan] {}".format(string))


def _userPrint(msg, _user=None):
    print("[{}] {}".format(user if _user is None else _user, msg))


def Login(user):
    global chatlists
    global userlist
    loginSuccess = False
    with grpc.insecure_channel(SERVER_ADDR) as channel:
        stub = chat_pb2_grpc.SpartanMessengerStub(channel)
        response = stub.LoginUser(chat_pb2.User(name=user, lastseen=0))
        _spartanPrint("Connected to Spartan Server at port {}.".format(SERVER_PORT))
    if response and len(response.groups) > 0:
        index = 0
        for chat in response.groups:
            LOG(LOG_DEBUG, "{}: Members: {} isGroup: {}".format(chat.groupid, chat.users, chat.isgroup))
            _members = list()
            for _user in chat.users:
                if chat.isgroup == False and _user.name == user:
                    continue
                _members.append(_user.name)
            _chatname = "{0}{1} {2}".format("Group: " if chat.isgroup else "1-1 with",
                                            chat.groupid if chat.isgroup else "",
                                            _members if chat.isgroup else _members[0])
            index = index + 1

            if chat.isgroup:
                groupid = chat.groupid
            else:
                groupid = _members[0]
            chat.lastmsgid = 0
            clientchats[groupid] = chat
        userlist = ",".join(clientchats.keys())
        loginSuccess = True
    else:
        LOG(LOG_INFO, "Unknown user {}".format(user))
    return loginSuccess


def PrintChats():
    global userlist
    _spartanPrint("User list: {}".format(userlist))


def _Input(prompt):
    res = None
    try:
        res = input(prompt)
    except (KeyboardInterrupt, EOFError) as e:
        print("\n")
    return res


def GetChat(groupid):
    return clientchats.get(groupid, None)


def CheckForChatRequests():
    chatrequest = None
    found = None
    for _groupid, _chat in clientchats.items():
        with grpc.insecure_channel(SERVER_ADDR) as channel:
            stub = chat_pb2_grpc.SpartanMessengerStub(channel)
            _lastid = _chat.lastmsgid
            recipient = _chat.groupid#Receiver
            msgs = stub.ReceiveMessage(chat_pb2.Message(
                sender=user, recipient=recipient,
                msg=None, msgid=_lastid))
            found = False
            for _msg in msgs:
                if _lastid < _msg.msgid:
                    # We have new messages on this chat, open this chat
                    found = True
                    break
            if found:
                chatrequest = _groupid
                break
    if found:
        res = _Input("[Spartan] {} is requesting to chat with you. "
                     "Enter 'yes' to accept or enter different user: ".format(chatrequest))
        if res is None:
            chatrequest = None
        elif res.strip('_') != "yes":
            # input is a different username
            chatrequest = res

    return chatrequest


def SendReceiveMsg():
    PrintChats()
    groupid = CheckForChatRequests()
    if groupid is None:
        groupid = _Input("[Spartan] Enter a user whom you want to chat with: ")
        if groupid is None:
            return False
        groupid = groupid.strip('_')

    # get chat entry for selected group
    chat = GetChat(groupid)
    LOG(LOG_DEBUG, "Chat  is : {}".format(chat))
    if chat is None:
        return False
    recipient = chat.groupid
    LOG(LOG_DEBUG, "Recipient is : {}".format(recipient))
    sender = user
    LOG(LOG_DEBUG, "Sender is : {}".format(sender))
    with grpc.insecure_channel(SERVER_ADDR) as channel:
        stub = chat_pb2_grpc.SpartanMessengerStub(channel)
        _spartanPrint("You are now ready to chat with {}.".format(groupid))
        # Query if there are any new messages before starting the chat
        msg = None
        _lastid = chat.lastmsgid
        LOG(LOG_DEBUG, "Last Msg ID before sending "
                       "message is : {}".format(_lastid))
        msgs = stub.ReceiveMessage(chat_pb2.Message(
            sender=sender, recipient=recipient,
            msg=msg,
            msgid=_lastid))
        for _msg in msgs:
            _lastid = _msg.msgid
            if _msg.sender and _msg.msg:
                _plaintext_msg = decrypt_message(key=chat.groupid, encrypted_message=_msg.msg)
                _userPrint("{}".format(_plaintext_msg.decode('utf-8')), _msg.sender)
            chat.lastmsgid = _lastid

        while True:
            _lastid = chat.lastmsgid
            msg = _Input("[{}] > ".format(sender))
            if msg is None:
                break
            if len(msg):
                msg = encrypt_message(key=chat.groupid, message=msg)
                LOG(LOG_DEBUG, "Encrypted message : {}".format(msg))
            else:
                msg = msg.encode('utf-8')
            msgs = stub.ReceiveMessage(chat_pb2.Message(
                sender=sender,
                recipient=recipient,
                msg=msg, msgid=_lastid))
            for _msg in msgs:
                _lastid = _msg.msgid
                if _msg.sender and _msg.msg:
                    _plaintext_msg = decrypt_message(key=chat.groupid, encrypted_message=_msg.msg)
                    _userPrint("{}".format(_plaintext_msg.decode('utf-8')), _msg.sender)
            # Save the msgid from the latest message for this chat
            chat.lastmsgid = _lastid
    return True


if __name__ == '__main__':
    if len(sys.argv) < 2:
        Usage(sys.argv[0])
        sys.exit(0)
    user = sys.argv[1]
    running = Login(user)
    while running is True:
        running = SendReceiveMsg()
