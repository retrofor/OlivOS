# -*- encoding: utf-8 -*-
"""
_______________________    ________________
__  __ \__  /____  _/_ |  / /_  __ \_  ___/
_  / / /_  /  __  / __ | / /_  / / /____ \
/ /_/ /_  /____/ /  __ |/ / / /_/ /____/ /
\____/ /_____/___/  _____/  \____/ /____/

@File      :   OlivOS/hook.py
@Author    :   lunzhiPenxil仑质
@Contact   :   lunzhipenxil@gmail.com
@License   :   AGPL
@Copyright :   (C) 2020-2023, OlivOS-Team
@Desc      :   None
"""

import os
import sys
import platform
import sqlite3
import pyjson5

from PIL import Image
from PyInstaller.utils.hooks import collect_all

if sys.platform == 'win32':
    import win32com.client
    import pythoncom
    import webview

if os.environ.get('OLIVOS_ENV_PACK') == "1":
    if sys.platform == 'win32':
        import winsound
    from lxml import etree
    import yaml
    import openpyxl
    import aiohttp
    import qrcode
    import certifi
    import httpx
    import prompt_toolkit
    import regex
    import rich
    import smtplib
    import email
    
    if os.environ.get('OLIVOS_ENV_DEBUG') != "1":
        # Are we running in a PyInstaller bundle
        # https://pyinstaller.org/en/stable/runtime-information.html#run-time-information
        if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):

            class NullOutput(object):
                def write(self, string):
                    pass

                def isatty(self):
                    return False

            sys.stdout = NullOutput()
            sys.stderr = NullOutput()

# collect all specific modules
def hook(hook_api):
    packages = ["email", "gevent", "sqlite3", "tkinter", "psutil"]
    for package in packages:
        datas, binaries, hiddenimports = collect_all(package)
        # hook_api.add_datas(datas)
        # hook_api.add_binaries(binaries)
        hook_api.add_imports(*hiddenimports)
