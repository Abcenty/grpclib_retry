# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streaming/helloworld.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1astreaming/helloworld.proto\x12\nhelloworld\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t2\xbd\x02\n\x07Greeter\x12H\n\x12UnaryUnaryGreeting\x12\x18.helloworld.HelloRequest\x1a\x16.helloworld.HelloReply\"\x00\x12K\n\x13UnaryStreamGreeting\x12\x18.helloworld.HelloRequest\x1a\x16.helloworld.HelloReply\"\x00\x30\x01\x12K\n\x13StreamUnaryGreeting\x12\x18.helloworld.HelloRequest\x1a\x16.helloworld.HelloReply\"\x00(\x01\x12N\n\x14StreamStreamGreeting\x12\x18.helloworld.HelloRequest\x1a\x16.helloworld.HelloReply\"\x00(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'streaming.helloworld_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_HELLOREQUEST']._serialized_start=42
  _globals['_HELLOREQUEST']._serialized_end=70
  _globals['_HELLOREPLY']._serialized_start=72
  _globals['_HELLOREPLY']._serialized_end=101
  _globals['_GREETER']._serialized_start=104
  _globals['_GREETER']._serialized_end=421
# @@protoc_insertion_point(module_scope)
