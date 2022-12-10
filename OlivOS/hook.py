# -*- encoding: utf-8 -*-
'''
_______________________    ________________
__  __ \__  /____  _/_ |  / /_  __ \_  ___/
_  / / /_  /  __  / __ | / /_  / / /____ \
/ /_/ /_  /____/ /  __ |/ / / /_/ /____/ /
\____/ /_____/___/  _____/  \____/ /____/

@File      :   OlivOS/hook.py
@Author    :   lunzhiPenxil仑质
@Contact   :   lunzhipenxil@gmail.com
@License   :   AGPL
@Copyright :   (C) 2020-2021, OlivOS-Team
@Desc      :   None
'''

import platform

#pillow
from PIL import Image

#lxml
from lxml import etree

#yaml
import yaml

#sqlite
import sqlite3

#openpyxl
import openpyxl

#aiohttp
import aiohttp

#qrcode
import qrcode

#win
if platform.system() == 'Windows':
    import win32com.client
    import pythoncom
