import os 
import subprocess

def shutdown_computer():
    if os.name == 'nt':
        print("windows")
        os.system("shutdown /s /t 0")
    elif os.name == "posix":
        print("macos")
        os.system("sudo shutdown -h now")
    else:
        print("Error, not mac/linux or windows")

shutdown_computer()