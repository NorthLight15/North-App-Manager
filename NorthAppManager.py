import os
import time
import sys
import json
import subprocess 
import SetupAssistant, src.colorfont as colorfont, installer
import distroCheck as distro
from src.filesTypes import Distro




print("Application install manager for Linux")

warningColor = colorfont.colors.WARNING
failColor = colorfont.colors.FAIL
NormalColor = colorfont.colors.END
OkeyColor = colorfont.colors.OKEY
Succsess = colorfont.colors.SUCCSESS


App = input("Application: ")
AppName = App.lower()

def fail_message():
    os.system("clear")
    print(f"{failColor}Application not found..{NormalColor}")

        

if __name__ == '__main__':

    

    distro = distro.Distro_check()

    if distro == Distro.Distro_ubuntu:
        
        try:
            installer.apt_installer(AppName)
            time.sleep(0.5)
        
        except:
            fail_message()

    else:
        
        if distro == Distro.Distro_debian:
           
            try:
                installer.apt_get_installer(AppName)
                time.sleep(0.5)
            
            except:
                fail_message()

        if distro == Distro.Distro_Fedora:
           
            try:
                installer.rpm_installer(AppName)
                time.sleep(0.5)
            
            except:
                fail_message()

        if distro == Distro.Distro_Arch:
            try:
                installer.pacman_installer(AppName)
                time.sleep(0.5)
            
            except:
                fail_message()

        else:
            print("Linux Distro not found...")



