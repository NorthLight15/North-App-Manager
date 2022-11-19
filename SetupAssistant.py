import colorfont
import subprocess
import os

errorMessage = f"{colorfont.colors.FAIL}There was a problem saving the file | It may be an unrecognized species, please let me know :) {colorfont.colors.END}"
sucsessMessage = f"{colorfont.colors.SUCCSESS}Extract Succsess{colorfont.colors.END}"


def extracter(AppName, ftype, commands, parameters):
        try:
            subprocess.check_call(f"{commands} {parameters} {AppName}{ftype}", shell=True)
            print(sucsessMessage)         
    
        except (OSError, subprocess.SubprocessError): 
            os.system("clear")
            print(errorMessage)

            
                    
    


