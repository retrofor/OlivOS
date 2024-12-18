# /// script
# requires-python = ">=3.8"
# dependencies = [
# "aiohttp>=3.10.11",
# "brotli>=1.1.0",
# "certifi>=2024.8.30",
# "filetype>=1.2.0",
# "flask>=2.2.5",
# "gevent>=24.2.1",
# "grpcio>=1.68.1",
# "grpcio-tools>=1.68.1",
# "httpx>=0.28.1",
# "js2py>=0.74",
# "lxml>=5.3.0",
# "openpyxl>=3.1.5",
# "pillow==9.3.0",
# "prompt-toolkit>=3.0.48",
# "protobuf>=5.29.1",
# "psutil>=6.1.0",
# "pybase64>=1.4.0",
# "pyinstaller>=6.11.1",
# "pyjson5>=1.6.7",
# "pystray>=0.19.5",
# "pywebview>=5.3.2",
# "pypiwin32; sys_platform == 'win32'",
# "pyyaml>=6.0.2",
# "qrcode>=7.4.2",
# "regex>=2024.11.6",
# "requests>=2.32.3",
# "requests-toolbelt>=1.0.0",
# "rich>=13.9.4",
# "rsa>=4.9",
# "websocket-client>=1.8.0",
# "websockets>=13.1",
# "werkzeug==2.2.2",
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
        _spec_or_python_file = platform_commands.get(_args[0] if _args else sys.platform, _args[0] if _args else "OlivOS.spec")
        # https://pyinstaller.org/en/stable/usage.html#running-pyinstaller-from-python-code
        PyInstaller.__main__.run(
            [
                _spec_or_python_file,
                "--clean",
                "--noconfirm",
                ]
            )

    def start(self) -> None:
        os.system("python main.py")

if __name__ == "__main__":
    command_list = sys.argv[1:]
    command_prefix = command_list[0]
    args = command_list[1:] or None
    if command_list:
        handle = CommandHandler(command_prefix=command_prefix)
        handle.execute(_args=args)
