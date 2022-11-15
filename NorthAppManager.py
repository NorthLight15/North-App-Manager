import sys
import json 
import pull
import installer
import xml.etree.cElementTree as xmlet

print("Application install manager for Linux")
print("-f for Mirror List")

userInput = input("User input: ")
#### Tested code ########


pull.SourcesListed(userInput)
installer.downloadder()

