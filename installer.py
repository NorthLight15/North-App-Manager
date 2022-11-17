import time
import subprocess
import random
import requests as req
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
    r = req.get(url)
    open(f"{filesName}", 'wb').write(r.content)

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


