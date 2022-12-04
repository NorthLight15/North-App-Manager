#!/bin/env python3

'''


We use this file to assemble elementary particles
This is the file that the end user will use.
All libraries are combined here to form a logical part and distribution controls are made here.



'''










import os
import time
import sys
import json
import subprocess 
import SetupAssistant, src.colorfont as colorfont, installer
import distroCheck as distro
from src.filesTypes import Distro

# Termianal font color 
warningColor = colorfont.colors.WARNING
failColor = colorfont.colors.FAIL
NormalColor = colorfont.colors.END
OkeyColor = colorfont.colors.OKEY
Succsess = colorfont.colors.SUCCSESS


attention = "Attention! Some of the applications you will download with this application have a user agreement, please pay attention to the user agreement of the application you will download."
print("Application install manager for Linux")
print(f"{warningColor}{attention}{NormalColor}")



App = input("Input : ")
AppName = App.lower()

def fail_message():
    # Fail system function.
    os.system("clear")
    print(f"{failColor}Application not found..{NormalColor}")

        

if __name__ == '__main__':

    # Distro check and controls. 

    
    try:
        distro = distro.Distro_check() # Distro check
    except:
        print(f"{warningColor}Distributed could not be checked{NormalColor}")
        try:
            installer.main_sources_installer(AppName)
        except:
            print(f"{failColor}Application not found...{NormalColor}")

        else:
            try:
                installer.pip_installer(App)
                print(f"{warningColor}Trying python pip installer{NormalColor}")
            except:
                print(f"{failColor}pip not working{NormalColor}")



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

    if distro == Distro.Distro_OpenSuse:
        installer.zypper_installer(AppName)
        time.sleep(0.5)



