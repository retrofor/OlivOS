# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command.proto
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\rcommand.proto\x12\x08vila_bot"&\n\nPHeartBeat\x12\x18\n\x10\x63lient_timestamp\x18\x01 \x01(\t"9\n\x0fPHeartBeatReply\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x18\n\x10server_timestamp\x18\x02 \x01(\x04"\xc0\x01\n\x06PLogin\x12\x0b\n\x03uid\x18\x01 \x01(\x04\x12\r\n\x05token\x18\x02 \x01(\t\x12\x10\n\x08platform\x18\x03 \x01(\x05\x12\x0e\n\x06\x61pp_id\x18\x04 \x01(\x05\x12\x11\n\tdevice_id\x18\x05 \x01(\t\x12\x0e\n\x06region\x18\x06 \x01(\t\x12(\n\x04meta\x18\x07 \x03(\x0b\x32\x1a.vila_bot.PLogin.MetaEntry\x1a+\n\tMetaEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"S\n\x0bPLoginReply\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x18\n\x10server_timestamp\x18\x03 \x01(\x04\x12\x0f\n\x07\x63onn_id\x18\x04 \x01(\x04"[\n\x07PLogout\x12\x0b\n\x03uid\x18\x01 \x01(\x04\x12\x10\n\x08platform\x18\x02 \x01(\x05\x12\x0e\n\x06\x61pp_id\x18\x03 \x01(\x05\x12\x11\n\tdevice_id\x18\x04 \x01(\t\x12\x0e\n\x06region\x18\x05 \x01(\t":\n\x0cPLogoutReply\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x0f\n\x07\x63onn_id\x18\x03 \x01(\x04"(\n\x0b\x43ommonReply\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t"(\n\x08PKickOff\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0e\n\x06reason\x18\x02 \x01(\t*\xf8\x01\n\x07\x43ommand\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x10\n\x0c\x45XCHANGE_KEY\x10\x01\x12\r\n\tHEARTBEAT\x10\x02\x12\t\n\x05LOGIN\x10\x03\x12\n\n\x06LOGOUT\x10\x04\x12\x12\n\x0eP_EXCHANGE_KEY\x10\x05\x12\x0f\n\x0bP_HEARTBEAT\x10\x06\x12\x0b\n\x07P_LOGIN\x10\x07\x12\x0c\n\x08P_LOGOUT\x10\x08\x12\x0c\n\x08KICK_OFF\x10\x33\x12\x0c\n\x08SHUTDOWN\x10\x34\x12\x0e\n\nP_KICK_OFF\x10\x35\x12\x0e\n\nROOM_ENTER\x10<\x12\x0e\n\nROOM_LEAVE\x10=\x12\x0e\n\nROOM_CLOSE\x10>\x12\x0c\n\x08ROOM_MSG\x10?B6Z4gopkg.mihoyo.com/vila-bot-go/proto/vila_bot;vila_botb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "command_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = (
        b"Z4gopkg.mihoyo.com/vila-bot-go/proto/vila_bot;vila_bot"
    )
    _PLOGIN_METAENTRY._options = None
    _PLOGIN_METAENTRY._serialized_options = b"8\001"
    _globals["_COMMAND"]._serialized_start = 644
    _globals["_COMMAND"]._serialized_end = 892
    _globals["_PHEARTBEAT"]._serialized_start = 27
    _globals["_PHEARTBEAT"]._serialized_end = 65
    _globals["_PHEARTBEATREPLY"]._serialized_start = 67
    _globals["_PHEARTBEATREPLY"]._serialized_end = 124
    _globals["_PLOGIN"]._serialized_start = 127
    _globals["_PLOGIN"]._serialized_end = 319
    _globals["_PLOGIN_METAENTRY"]._serialized_start = 276
    _globals["_PLOGIN_METAENTRY"]._serialized_end = 319
    _globals["_PLOGINREPLY"]._serialized_start = 321
    _globals["_PLOGINREPLY"]._serialized_end = 404
    _globals["_PLOGOUT"]._serialized_start = 406
    _globals["_PLOGOUT"]._serialized_end = 497
    _globals["_PLOGOUTREPLY"]._serialized_start = 499
    _globals["_PLOGOUTREPLY"]._serialized_end = 557
    _globals["_COMMONREPLY"]._serialized_start = 559
    _globals["_COMMONREPLY"]._serialized_end = 599
    _globals["_PKICKOFF"]._serialized_start = 601
    _globals["_PKICKOFF"]._serialized_end = 641
# @@protoc_insertion_point(module_scope)
