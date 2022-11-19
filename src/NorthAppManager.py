import os
import time
import sys
import json 
import SetupAssistant as SetupAssistant, colorfont, installer




print("Application install manager for Linux")

warningColor = colorfont.colors.WARNING
failColor = colorfont.colors.FAIL
NormalColor = colorfont.colors.END
OkeyColor = colorfont.colors.OKEY
Succsess = colorfont.colors.SUCCSESS


AppName = input("Application: ")


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
        installer.pacman_installer(AppName)
        time.sleep(0.5)
        try:
            print(f"{OkeyColor}Wait...{NormalColor}")
            installer.main_sources_installer(AppName)
            print(f"{Succsess}Installed and Succsess configration...{NormalColor}")
        except:
                print(f"{warningColor}Application not found..{NormalColor}")

                    



