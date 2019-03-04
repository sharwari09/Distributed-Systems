# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chat.proto',
  package='messenger',
  syntax='proto3',
  serialized_pb=_b('\n\nchat.proto\x12\tmessenger\"H\n\x07Message\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x11\n\trecipient\x18\x02 \x01(\t\x12\x0b\n\x03msg\x18\x03 \x01(\x0c\x12\r\n\x05msgid\x18\x04 \x01(\x04\"&\n\x04User\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08lastseen\x18\x02 \x01(\x04\"\\\n\x05Group\x12\x1e\n\x05users\x18\x01 \x03(\x0b\x32\x0f.messenger.User\x12\x0f\n\x07groupid\x18\x02 \x01(\t\x12\x0f\n\x07isgroup\x18\x03 \x01(\x08\x12\x11\n\tlastmsgid\x18\x04 \x01(\x03\"*\n\x06Groups\x12 \n\x06groups\x18\x01 \x03(\x0b\x32\x10.messenger.Group2\x83\x01\n\x10SpartanMessenger\x12\x31\n\tLoginUser\x12\x0f.messenger.User\x1a\x11.messenger.Groups\"\x00\x12<\n\x0eReceiveMessage\x12\x12.messenger.Message\x1a\x12.messenger.Message\"\x00\x30\x01\x62\x06proto3')
)




_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='messenger.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='messenger.Message.sender', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recipient', full_name='messenger.Message.recipient', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg', full_name='messenger.Message.msg', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msgid', full_name='messenger.Message.msgid', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=97,
)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='messenger.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='messenger.User.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lastseen', full_name='messenger.User.lastseen', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=137,
)


_GROUP = _descriptor.Descriptor(
  name='Group',
  full_name='messenger.Group',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='users', full_name='messenger.Group.users', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='groupid', full_name='messenger.Group.groupid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isgroup', full_name='messenger.Group.isgroup', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lastmsgid', full_name='messenger.Group.lastmsgid', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=231,
)


_GROUPS = _descriptor.Descriptor(
  name='Groups',
  full_name='messenger.Groups',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='groups', full_name='messenger.Groups.groups', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=233,
  serialized_end=275,
)

_GROUP.fields_by_name['users'].message_type = _USER
_GROUPS.fields_by_name['groups'].message_type = _GROUP
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['Group'] = _GROUP
DESCRIPTOR.message_types_by_name['Groups'] = _GROUPS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'chat_pb2'
  # @@protoc_insertion_point(class_scope:messenger.Message)
  ))
_sym_db.RegisterMessage(Message)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), dict(
  DESCRIPTOR = _USER,
  __module__ = 'chat_pb2'
  # @@protoc_insertion_point(class_scope:messenger.User)
  ))
_sym_db.RegisterMessage(User)

Group = _reflection.GeneratedProtocolMessageType('Group', (_message.Message,), dict(
  DESCRIPTOR = _GROUP,
  __module__ = 'chat_pb2'
  # @@protoc_insertion_point(class_scope:messenger.Group)
  ))
_sym_db.RegisterMessage(Group)

Groups = _reflection.GeneratedProtocolMessageType('Groups', (_message.Message,), dict(
  DESCRIPTOR = _GROUPS,
  __module__ = 'chat_pb2'
  # @@protoc_insertion_point(class_scope:messenger.Groups)
  ))
_sym_db.RegisterMessage(Groups)



_SPARTANMESSENGER = _descriptor.ServiceDescriptor(
  name='SpartanMessenger',
  full_name='messenger.SpartanMessenger',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=278,
  serialized_end=409,
  methods=[
  _descriptor.MethodDescriptor(
    name='LoginUser',
    full_name='messenger.SpartanMessenger.LoginUser',
    index=0,
    containing_service=None,
    input_type=_USER,
    output_type=_GROUPS,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ReceiveMessage',
    full_name='messenger.SpartanMessenger.ReceiveMessage',
    index=1,
    containing_service=None,
    input_type=_MESSAGE,
    output_type=_MESSAGE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SPARTANMESSENGER)

DESCRIPTOR.services_by_name['SpartanMessenger'] = _SPARTANMESSENGER

try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class SpartanMessengerStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.LoginUser = channel.unary_unary(
          '/messenger.SpartanMessenger/LoginUser',
          request_serializer=User.SerializeToString,
          response_deserializer=Groups.FromString,
          )
      self.ReceiveMessage = channel.unary_stream(
          '/messenger.SpartanMessenger/ReceiveMessage',
          request_serializer=Message.SerializeToString,
          response_deserializer=Message.FromString,
          )


  class SpartanMessengerServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def LoginUser(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def ReceiveMessage(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_SpartanMessengerServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'LoginUser': grpc.unary_unary_rpc_method_handler(
            servicer.LoginUser,
            request_deserializer=User.FromString,
            response_serializer=Groups.SerializeToString,
        ),
        'ReceiveMessage': grpc.unary_stream_rpc_method_handler(
            servicer.ReceiveMessage,
            request_deserializer=Message.FromString,
            response_serializer=Message.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'messenger.SpartanMessenger', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaSpartanMessengerServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def LoginUser(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def ReceiveMessage(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaSpartanMessengerStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def LoginUser(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    LoginUser.future = None
    def ReceiveMessage(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()


  def beta_create_SpartanMessenger_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('messenger.SpartanMessenger', 'LoginUser'): User.FromString,
      ('messenger.SpartanMessenger', 'ReceiveMessage'): Message.FromString,
    }
    response_serializers = {
      ('messenger.SpartanMessenger', 'LoginUser'): Groups.SerializeToString,
      ('messenger.SpartanMessenger', 'ReceiveMessage'): Message.SerializeToString,
    }
    method_implementations = {
      ('messenger.SpartanMessenger', 'LoginUser'): face_utilities.unary_unary_inline(servicer.LoginUser),
      ('messenger.SpartanMessenger', 'ReceiveMessage'): face_utilities.unary_stream_inline(servicer.ReceiveMessage),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_SpartanMessenger_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('messenger.SpartanMessenger', 'LoginUser'): User.SerializeToString,
      ('messenger.SpartanMessenger', 'ReceiveMessage'): Message.SerializeToString,
    }
    response_deserializers = {
      ('messenger.SpartanMessenger', 'LoginUser'): Groups.FromString,
      ('messenger.SpartanMessenger', 'ReceiveMessage'): Message.FromString,
    }
    cardinalities = {
      'LoginUser': cardinality.Cardinality.UNARY_UNARY,
      'ReceiveMessage': cardinality.Cardinality.UNARY_STREAM,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'messenger.SpartanMessenger', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)