from shutil import copytree
import time
from datetime import datetime
from sys import exit

original = r'C:\Users\charl\AppData\Roaming\DarkSoulsIII\0110000103a1776a'
targetpath = r'E:\Mes documents\Dark Souls 3 - save files\SafeCopy\save'

while True:

    try:
        CurDT = datetime.now()
        safe_time = CurDT.strftime("%Y-%m-%d %Hh %Mm %Ss")

        copytree(original, targetpath + " " + safe_time)

    except IOError as e:
        print("Unable to copy file. %s" % e)
        exit(1)
    except:
        print("Unexpected error:", sys.exc_info())
        exit(1)

    print("\nFile was safely copied!\n")
    print("\nNext save in: 15min\n")
    time.sleep(900)
    print("\nNext save in: 10min\n")
    time.sleep(600)
    print("\nNext save in: 5min\n")
    time.sleep(300)