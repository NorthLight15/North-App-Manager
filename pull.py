import random
import requests as req
import yaml
from yaml import Loader
import urllib.request
def SourcesDownload(App):

    file = open("AppSources/sources.yaml")
    data = yaml.load(file, Loader=Loader)

    # Application find for Searching code
    AppName = data[App][3] # Sources Application name
    link = data[App][1] # Sources Application direct link
    filesType = data[App][2] # Sources Application files type

    filesName = f"{AppName}{filesType}" # Combines the application name with the file type

    url = link
    r = req.get(url)
    open(filesName, 'wb').write(r.content)






                            
