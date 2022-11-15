import random
import json
import requests as req
import xml.etree.cElementTree as xmlet

def SourcesDownload(App, File):

    tree = xmlet.parse("AppSources/sources.xml")
    sources = tree.getroot()

    tag = sources.tag
    attr = sources.attrib

    # Application find for Searching code

    try:
        for value in sources.findall(App): # searches for a given value
            AppLink = value.find("link").text # Receives and uses the link
            r = req.get(AppLink, allow_redirects=True)
            open(File, "wb").write(r.content) # Not tested

    except:
        print("Not Result")
