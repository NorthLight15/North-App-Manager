import os
import time
import sys
import json 
import colorfont
import installer


print("Application install manager for Linux")

warningColor = colorfont.colors.WARNING
failColor = colorfont.colors.FAIL
NormalColor = colorfont.colors.END
OkeyColor = colorfont.colors.OKEY
Succsess = colorfont.colors.SUCCSESS


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
            print(f"{Succsess}Installed....{NormalColor}")
        except:
            print(f"{failColor}Application not founded{NormalColor}")
                    



