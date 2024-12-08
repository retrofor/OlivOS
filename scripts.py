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
import PyInstaller.__main__

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
            "win32": "OlivOS.spec",
            "linux": "OlivOS_linux.spec",
            "darwin": "OlivOS_mac.spec",
            "debug": "OlivOS_debug.spec"
        }
        _spec_or_python_file = platform_commands.get((_args[0] if _args else sys.platform), _args[0])
        # https://pyinstaller.org/en/stable/usage.html#running-pyinstaller-from-python-code
        PyInstaller.__main__.run(
            [
                _spec_or_python_file,
                "--clean",
                "--noconfirm",
                ].append(_args[1:] if _args else [])
            )

    def start(self) -> None:
        os.system("python main.py")

if __name__ == "__main__":
    command_list = sys.argv[1:]
    command_prefix = command_list[0]
    args = command_list[1:]
    if command_list:
        handle = CommandHandler(command_prefix=command_prefix)
        handle.execute(args)