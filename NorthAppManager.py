#!/bin/env python3
import os
import time
import sys
import json
import subprocess 
import SetupAssistant, src.colorfont as colorfont, installer
import distroCheck as distro
from src.filesTypes import Distro


warningColor = colorfont.colors.WARNING
failColor = colorfont.colors.FAIL
NormalColor = colorfont.colors.END
OkeyColor = colorfont.colors.OKEY
Succsess = colorfont.colors.SUCCSESS


attention = "Attention! Some of the applications you will download with this application have a user agreement, please pay attention to the user agreement of the application you will download."
print("Application install manager for Linux")
print(f"{warningColor}{attention}{NormalColor}")



App = input("Application: ")
AppName = App.lower()

def fail_message():
    os.system("clear")
    print(f"{failColor}Application not found..{NormalColor}")

        

if __name__ == '__main__':

    
    try:
        distro = distro.Distro_check()
    except:
        print(f"{warningColor}Distributed could not be checked{NormalColor}")
        try:
            installer.main_sources_installer(AppName)
        except:
            print(f"{failColor}Application not found...{NormalColor}")


    if distro == Distro.Distro_ubuntu:
            installer.apt_installer(AppName)
            time.sleep(0.5)
    
    if distro == Distro.Distro_debian:

                installer.apt_get_installer(AppName)
                time.sleep(0.5)
            
    if distro == Distro.Distro_Fedora:
                installer.rpm_installer(AppName)
                time.sleep(0.5)
            

    if distro == Distro.Distro_Arch:
                installer.pacman_installer(AppName)
                time.sleep(0.5)



