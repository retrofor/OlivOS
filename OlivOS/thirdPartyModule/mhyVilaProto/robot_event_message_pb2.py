# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: robot_event_message.proto
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import model_pb2 as model__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x19robot_event_message.proto\x12\x08vila_bot\x1a\x0bmodel.proto"8\n\x11RobotEventMessage\x12#\n\x05\x65vent\x18\x01 \x01(\x0b\x32\x14.vila_bot.RobotEventB6Z4gopkg.mihoyo.com/vila-bot-go/proto/vila_bot;vila_botb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "robot_event_message_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = (
        b"Z4gopkg.mihoyo.com/vila-bot-go/proto/vila_bot;vila_bot"
    )
    _globals["_ROBOTEVENTMESSAGE"]._serialized_start = 52
    _globals["_ROBOTEVENTMESSAGE"]._serialized_end = 108
# @@protoc_insertion_point(module_scope)
