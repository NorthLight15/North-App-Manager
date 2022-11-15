import sys
import json 
import pull

userInput = input("User input: ")

print("Application install manager for Linux")
print("-f for Mirror List")
#### Tested code

if userInput == "-f":
    pull.SourcesListed()

