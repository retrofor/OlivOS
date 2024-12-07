# /// script
# requires-python = ">=3.8"
# dependencies = [
#   "OlivOS",
#   "pyinstaller",
# ]
# ///

from __future__ import annotations

import os
import sys
import OlivOS  # noqa: F401
from typing import Any, Awaitable, Callable, List, Optional


class CommandHandler:
    def __init__(self, command_prefix: str) -> None:
        self.command_prefix = command_prefix

    def __getattr__(self, item: str) -> Callable[..., Awaitable[Any]]:
        return getattr(self, item, None)
    
    def execute(self, _args: Optional[List[str]]) -> None:
        getattr(self, self.command_prefix, None)(_args)

    def build(self, _args: Optional[List[str]] = None) -> None:
        platform_commands = {
            "win32": "pyinstaller main.spec",
            "linux": "pyinstaller main_linux.spec",
            "darwin": "pyinstaller main_mac.spec",
            "debug": "pyinstaller main_debug.spec"
        }
        os.system(platform_commands.get((_args[0] if _args else sys.platform), "echo Unsupported platform"))

    def start(self) -> None:
        os.system("python main.py")

if __name__ == "__main__":
    command_list = sys.argv[1:]
    command_prefix = command_list[0]
    args = command_list[1:]
    if command_list:
        handle = CommandHandler(command_prefix=command_prefix)
        handle.execute(args)