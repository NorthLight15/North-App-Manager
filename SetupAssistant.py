import colorfont
import subprocess
import os
import time
errorMessage = f"{colorfont.colors.FAIL}There was a problem saving the file | It may be an unrecognized species, please let me know :) {colorfont.colors.END}"
sucsessMessage = f"{colorfont.colors.SUCCSESS}Extract Succsess{colorfont.colors.END}"


def extracter(commands, parameters, AppName, ftype):
        
        
        osCommand = f"{commands} {parameters} {AppName}{ftype}"
        
        try:
            subprocess.check_call(osCommand, shell=True)
            print(sucsessMessage)         
    
        except (OSError, subprocess.SubprocessError): 
            print(errorMessage)


            
                    
    


