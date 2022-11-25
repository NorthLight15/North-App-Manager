
"""
This file is mainly for download.
Documentation in the AppSources.yaml version splits the data into pieces and creates a full filename
Then a request is sent to the link and the file is downloaded over the request.

After downloading, the file is extracted with the filename in AppSources and the SetupAssistant file.

If there is that application in the package manager, download and install it directly from the package manager.




"""










import time
import subprocess
import random
import requests as req
import SetupAssistant 
import yaml
import os
import src.colorfont as colorfont
import distroCheck as distro
from src.filesTypes import FilesType as ft # Files Type detector function
from src.filesTypes import Commands as cmd 
from src.filesTypes import Paremeters as param
from src.filesTypes import Distro
from yaml import Loader
import sys

warningColor = colorfont.colors.WARNING
failColor = colorfont.colors.FAIL
NormalColor = colorfont.colors.END
OkeyColor = colorfont.colors.OKEY
Succsess = colorfont.colors.SUCCSESS




def main_sources_installer(App):

    file = open("AppSources/sources.yaml")
    data = yaml.load(file, Loader=Loader)

    # Application find for Searching code
    
    
    developer = data[App][0] # Sources developer name 
    AppName = data[App][3] # Sources Application name
    link = data[App][1] # Sources Application direct link
    filesType = data[App][2] # Sources Application files type
    
    

    filesName = f"{AppName}{filesType}" # Combines the application name with the file type

    url = link
    try:
        print(f"{Succsess}Download started... Please not closed{NormalColor}")
        print(f"Download Link: {link}")
        r = req.get(url) # Request for Download

    except:
        print(f"{failColor}We encountered an unknown error...{NormalColor}")
    try:
        print(f"{OkeyColor}Downloading and saving file...{NormalColor}")
        open(f"{filesName}", 'wb').write(r.content) # Saves the computer
    
        


        # Performs operations by file type

        if filesType == ft.tar_gz:
            SetupAssistant.extracter(cmd.command_tar_gz, param.Paremeter_tar_gz, AppName, filesType)

        if filesType == ft.tar_xz:
            SetupAssistant.extracter(cmd.command_tar_xz,param.Parameter_tar_xz,AppName, filesType)
        
        if filesType == ft.tar_bz2:
            SetupAssistant.extracter(cmd.command_tar_bz2, param.Parameter_tar_bz2, AppName, filesType)
        
        if filesType == ft.deb:
            SetupAssistant.extracter(cmd.commnad_deb,param.Parameter_deb,AppName, filesType)
        
        if filesType == ft.rpm:
            SetupAssistant.extracter(cmd.command_rpm,param.Parameter_rpm,AppName, filesType)
        
        if filesType == ft.zip:
            SetupAssistant.extracter(cmd.command.zip,param.Parameter_zip,AppName, filesType)

    except:
        print(f"{failColor}There was a problem saving the file{NormalColor}")

        SetupAssistant.installersh_setup(App) #setup manager.


# It checks these before looking at its own sources.


def apt_installer(App):
   
    print(f"{OkeyColor}Trying apt{NormalColor}")
    try:              
        subprocess.check_call(f"sudo apt install {App}", shell=True)
        print(f"{Succsess}Downloaded...{NormalColor}")         
    
    except (OSError, subprocess.SubprocessError): 
        print(f"{warningColor}apt not working..{NormalColor}")
        main_sources_installer(App)
    

      



def apt_get_installer(App):
        print(f"{OkeyColor}Trying apt-get{NormalColor}")
        try:              
            subprocess.check_call(f"sudo apt-get install {App}", shell=True)

        except (OSError, subprocess.SubprocessError): 
            print(f"{warningColor}apt-get not working..{NormalColor}")
            main_sources_installer(App)
            

    


def dnf_installer(App):
        print(f"{OkeyColor}Trying dnf{NormalColor}")
        try:              
            subprocess.check_call(f"sudo dnf install {App}", shell=True)         
        except (OSError, subprocess.SubprocessError): 
            print(f"{warningColor}dnf not working..{NormalColor}")
            main_sources_installer(App)
            

       



def pacman_installer(App):
            
            print(f"{OkeyColor}Trying pacman{NormalColor}")
            try:              
                subprocess.check_call(f"sudo pacman -S {App}", shell=True)         
            except (OSError, subprocess.SubprocessError): 
                print(f"{warningColor}pacman not working..{NormalColor}")
                main_sources_installer(App)
                

def zypper_installer(App):
    print(f"{OkeyColor} Trying zypper{NormalColor}")
    
    try:
        subprocess.check_call(f"sudo zypper in {App}", shell= True)
    except (OSError, subprocess.SubprocessError):
        print(f"{warningColor}zypper not working... {NormalColor}")
        main_sources_installer(App)
        
