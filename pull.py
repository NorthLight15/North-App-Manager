import random
import json
import xml.etree.cElementTree as xmlet

def SourcesListed(userInput):

    tree = xmlet.parse("AppSources/sources.xml")
    sources = tree.getroot()

    tag = sources.tag
    attr = sources.attrib

    # Application find for Searching code

    try:
        for i in sources.findall(userInput): # searches for a given value
            print(i.find("link").text) # Receives and uses the link
    except:
        print("Not Result")
