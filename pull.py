import random
import json

def SourcesListed():
    appSources = open("AppSources/sources.json")
    data = json.load(appSources)

    for i in data["Application"]:
        print(i)

    appSources.close()