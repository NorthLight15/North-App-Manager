import colorfont
import subprocess
import os


def setup(AppName):

    failValue = 0

    try:
        subprocess.check_call(f"tar -xzf {AppName}.tar.gz", shell=True)
        print(f"{colorfont.colors.SUCCSESS}Extract Succsess{colorfont.colors.END}")         
    
    except (OSError, subprocess.SubprocessError): 
        os.system("clear")
        print(f"{colorfont.colors.FAIL}There was a problem saving the file | It may be an unrecognized species, please let me know :) {colorfont.colors.END}")
        failValue = + failValue + 1   
        print(failValue) 

        return failValue