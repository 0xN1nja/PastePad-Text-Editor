"""
File : setup.py
Author : Abhimanyu Sharma
GitHub : https://github.com/0xN1nja
"""
import cx_Freeze
import sys
import os

base = None
if sys.platform == 'win32':
    base = "Win32GUI"
os.environ['TCL_LIBRARY'] = r"C:\Users\speed\AppData\Local\Programs\Python\Python310\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\speed\AppData\Local\Programs\Python\Python310\tcl\tk8.6"
executables = [cx_Freeze.Executable("pastepad.py", base=base, icon="icon.ico")]
cx_Freeze.setup(
    name="PastePad Text Editor",
    options={"build_exe": {"packages": ["tkinter", "os", "webbrowser", "datetime"],
                           "include_files": ["icon.ico", 'tcl86t.dll', 'tk86t.dll', 'icons2']}},
    version="0.0.14",
    author="Abhimanyu Sharma",
    description="PastePad Text Editor",
    executables=executables
)