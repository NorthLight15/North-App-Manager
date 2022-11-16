import time
import subprocess
import random
import requests as req
import yaml
import os
from yaml import Loader


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
   
    try:              
        subprocess.check_call(f"sudo apt install {App}", shell=True)         
    except (OSError, subprocess.SubprocessError): 
        print("apt not working..")             

def apt_get_installer(App):
        try:              
            subprocess.check_call(f"sudo apt-get install {App}", shell=True)         
        except (OSError, subprocess.SubprocessError): 
            print("apt-get not working..")

def dnf_installer(App):
        try:              
            subprocess.check_call(f"sudo dnf install {App}", shell=True)         
        except (OSError, subprocess.SubprocessError): 
            print("dnf not working..")


