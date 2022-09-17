""" Write a Python program to get the Python version you are using"""
from platform import platform, python_version, libc_ver
import platform
import sys

def check_python_verison():
    version_py = sys.version
    print("python version",version_py)
    print("python version",python_version())
    print("version_info",sys.version_info)
    print("libic ver",libc_ver())

""" Write a Python program to display the current date and time."""

def show_currrent_time():
    from datetime import datetime
    import time
    t = time.localtime()  #returns time with date and time
    c_time = time.strftime("%H:hrs, %M:min, %S: second, %y:year, %m:month, %d:day",t)
    print(c_time)
    now = datetime.now()
    print(platform._comparable_version)
    current_time = "current time: " + now.strftime("%H:hours %M: minutes %S:secods ")
    return current_time

print(show_currrent_time())