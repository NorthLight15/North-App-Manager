import random
import requests as req
import yaml
from yaml import Loader
import urllib.request
def SourcesDownload(App):

    file = open("AppSources/sources.yaml")
    data = yaml.load(file, Loader=Loader)

    # Application find for Searching code
    AppName = data[App][0]
    link = data[App][1]
    filesType = data[App][2]

    url = link
    r = req.get(url)
    open("code.tar.xz", 'wb').write(r.content) # Burada

# Dosya ismi belirlemede kaldın




                            
