import time
import subprocess
import random
import requests as req
import SetupAssistant
import yaml
import os
import colorfont
from yaml import Loader



warningColor = colorfont.colors.WARNING
failColor = colorfont.colors.FAIL
NormalColor = colorfont.colors.END
OkeyColor = colorfont.colors.OKEY
Succsess = colorfont.colors.SUCCSESS


def main_sources_installer(App):

    file = open("AppSources/sources.yaml")
    data = yaml.load(file, Loader=Loader)

    # Application find for Searching code
    AppName = data[App][3] # Sources Application name
    link = data[App][1] # Sources Application direct link
    filesType = data[App][2] # Sources Application files type

    filesName = f"{AppName}{filesType}" # Combines the application name with the file type

    url = link
    try:
        print(f"{Succsess}Download started... Please not closed{NormalColor}")
        r = req.get(url)
    except:
        print(f"{failColor}We encountered an unknown error...{NormalColor}")
    try:
        print(f"{OkeyColor}Downloading and saving file...{NormalColor}")
        open(f"{filesName}", 'wb').write(r.content)
        SetupAssistant.setup(AppName)
    except:
        print(f"{failColor}There was a problem saving the file{NormalColor}")



def apt_installer(App):
   
    print(f"{OkeyColor}Trying apt{NormalColor}")
    try:              
        subprocess.check_call(f"sudo apt install {App}", shell=True)
        print(f"{Succsess}Downloaded...{NormalColor}")         
    except (OSError, subprocess.SubprocessError): 
        print(f"{warningColor}apt not working..{NormalColor}")             



def apt_get_installer(App):
        print(f"{OkeyColor}Trying apt-get{NormalColor}")
        try:              
            subprocess.check_call(f"sudo apt-get install {App}", shell=True)
            print("")         
        except (OSError, subprocess.SubprocessError): 
            print(f"{warningColor}apt-get not working..{NormalColor}")



def dnf_installer(App):
        print(f"{OkeyColor}Trying dnf{NormalColor}")
        try:              
            subprocess.check_call(f"sudo dnf install {App}", shell=True)         
        except (OSError, subprocess.SubprocessError): 
            print(f"{warningColor}dnf not working..{NormalColor}")



def pacman_installer(App):
            
            print(f"{OkeyColor}Trying pacman{NormalColor}")
            try:              
                subprocess.check_call(f"sudo pacman -S {App}", shell=True)         
            except (OSError, subprocess.SubprocessError): 
                print(f"{warningColor}pacman not working..{NormalColor}")


