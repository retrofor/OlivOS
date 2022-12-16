# -*- encoding: utf-8 -*-
'''
_______________________    ________________
__  __ \__  /____  _/_ |  / /_  __ \_  ___/
_  / / /_  /  __  / __ | / /_  / / /____ \
/ /_/ /_  /____/ /  __ |/ / / /_/ /____/ /
\____/ /_____/___/  _____/  \____/ /____/

@File      :   OlivOS/biliLiveSDK.py
@Author    :   lunzhiPenxil仑质
@Contact   :   lunzhipenxil@gmail.com
@License   :   AGPL
@Copyright :   (C) 2020-2021, OlivOS-Team
@Desc      :   None
'''

import OlivOS

import time


class bot_info_T(object):
    def __init__(self, id = -1, room_id = None):
        self.id = id
        self.room_id = room_id
        self.debug_mode = False
        self.debug_logger = None

def get_SDK_bot_info_from_Plugin_bot_info(plugin_bot_info):
    res = bot_info_T(
        plugin_bot_info.id,
        plugin_bot_info.post_info.access_token
    )
    res.debug_mode = plugin_bot_info.debug_mode
    return res

def get_SDK_bot_info_from_Event(target_event):
    res = bot_info_T(
        target_event.bot_info.id,
        target_event.bot_info.post_info.access_token
    )
    res.debug_mode = target_event.bot_info.debug_mode
    return res

class event(object):
    def __init__(self, payload_data = None, bot_info = None):
        self.payload = payload_data
        self.platform = {}
        self.platform['sdk'] = 'biliLive_link'
        self.platform['platform'] = 'biliLive'
        self.platform['model'] = 'default'
        self.active = False
        if self.payload != None:
            self.active = True
        self.base_info = {}
        if self.active:
            self.base_info['time'] = int(time.time())
            self.base_info['self_id'] = bot_info.id
            self.base_info['room_id'] = bot_info.post_info.access_token
            self.base_info['post_type'] = None

class BiliLiveBot(OlivOS.thirdPartyModule.blivedm.BLiveClient):
    def __init__(
            self,
            room_id,
            uid = 0,
            session = None, 
            heartbeat_interval = 30,
            ssl = True,
            loop = None,
            Proc = None
        ):
        super().__init__(
            room_id,
            uid = uid,
            session = session,
            heartbeat_interval = heartbeat_interval,
            ssl = ssl,
            loop = loop
        )
        self.Proc = Proc
        handler = SDKHandler()
        self.add_handler(handler)

class SDKHandler(OlivOS.thirdPartyModule.blivedm.BaseHandler):
    async def _on_danmaku(self, client:BiliLiveBot, message:OlivOS.thirdPartyModule.blivedm.models.DanmakuMessage):
        try:
            sdk_event = event(message, client.Proc.Proc_data['bot_info_dict'])
            tx_packet_data = OlivOS.pluginAPI.shallow.rx_packet(sdk_event)
            client.Proc.Proc_info.tx_queue.put(tx_packet_data, block = False)
        except Exception as e:
            pass

def get_Event_from_SDK(target_event:event):
    target_event.base_info['time'] = target_event.sdk_event.base_info['time']
    target_event.base_info['self_id'] = str(target_event.sdk_event.base_info['self_id'])
    target_event.base_info['type'] = target_event.sdk_event.base_info['post_type']
    target_event.platform['sdk'] = target_event.sdk_event.platform['sdk']
    target_event.platform['platform'] = target_event.sdk_event.platform['platform']
    target_event.platform['model'] = target_event.sdk_event.platform['model']
    target_event.plugin_info['message_mode_rx'] = 'olivos_string'
    plugin_event_bot_hash = OlivOS.API.getBotHash(
        bot_id = target_event.base_info['self_id'],
        platform_sdk = target_event.platform['sdk'],
        platform_platform = target_event.platform['platform'],
        platform_model = target_event.platform['model']
    )
    type_sdk_event = type(target_event.sdk_event.payload)
    if type_sdk_event == OlivOS.thirdPartyModule.blivedm.models.DanmakuMessage:
        sdk_payload:OlivOS.thirdPartyModule.blivedm.models.DanmakuMessage = target_event.sdk_event.payload
        target_event.active = True
        target_event.plugin_info['func_type'] = 'group_message'
        message_obj = OlivOS.messageAPI.Message_templet('olivos_string', sdk_payload.msg)
        target_event.data = target_event.group_message(
            str(target_event.sdk_event.base_info['self_id']),
            str(sdk_payload.uid),
            sdk_payload.msg,
            'group'
        )
        target_event.data.message_sdk = message_obj
        target_event.data.message_id = '-1'
        target_event.data.raw_message = sdk_payload.msg
        target_event.data.raw_message_sdk = message_obj
        target_event.data.font = None
        target_event.data.sender['user_id'] = str(sdk_payload.uid)
        target_event.data.sender['nickname'] = str(sdk_payload.uname)
        target_event.data.sender['id'] = str(sdk_payload.uid)
        target_event.data.sender['name'] = str(sdk_payload.uname)
        target_event.data.sender['sex'] = 'unknown'
        target_event.data.sender['age'] = 0
        target_event.data.sender['role'] = 'member'
        target_event.data.host_id = None
