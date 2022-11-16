import sys
import json 
import pull
import xml.etree.cElementTree as xmlet

print("Application install manager for Linux")

AppName = input("Application: ")

#### Tested code ########


if __name__ == '__main__':
    
    pull.SourcesDownload(AppName)

