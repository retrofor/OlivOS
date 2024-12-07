# /// script
# requires-python = ">=3.8"
# dependencies = [
#   "OlivOS",
#   "pyinstaller",
# ]
# ///

import os
import sys
import OlivOS

command_list = sys.argv[1:]

if command_list[0] == "build":
    if sys.platform == "win32":
        os.system("pyinstaller main.spec")
    elif sys.platform == "linux":
        os.system("pyinstaller main_linux.spec")
    elif sys.platform == "darwin":
        os.system("pyinstaller main_mac.spec")
if command_list[0] == "start":
    os.system("python main.py")