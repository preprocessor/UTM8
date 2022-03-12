
#! build.py

import sys

from cx_Freeze import Executable, setup

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("utm8gui.pyw", icon='./data/icon.ico', base=base)]

setup(
    name="UTM8",
    version="1.0",
    description="UTM8",
    executables=executables,
)
