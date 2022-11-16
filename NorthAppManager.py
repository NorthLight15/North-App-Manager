import sys
import json 
import pull
import xml.etree.cElementTree as xmlet

print("Application install manager for Linux")
print("-f for Mirror List")

AppName = input("Application: ")
#fileName = input("Downloaded file name:")
#### Tested code ########


pull.SourcesDownload(AppName)

