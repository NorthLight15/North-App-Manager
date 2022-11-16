import os
import time
import sys
import json 
import installer
import configration


print("Application install manager for Linux")


AppName = input("Application: ")

#### Tested code ########


if __name__ == '__main__':
        
    os.system("clear")
    try:
        installer.apt_installer(AppName)
        time.sleep(0.5)
    except: 
        installer.apt_get_installer(AppName)
        time.sleep(0.5)
    else:
        installer.dnf_installer(AppName)
        time.sleep(0.5)
        try:
            installer.main_sources_installer(AppName)
        except:
            print("Application not founded")
                    



