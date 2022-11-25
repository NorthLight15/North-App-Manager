'''


It is designed for file separation and installation.

It performs file extraction by working without being seen in the terminal.

'''




import src.colorfont as colorfont
import src.filesTypes as filesTypes
import subprocess
import os
import time


errorMessage = f"{colorfont.colors.FAIL}There was a problem saving the file | It may be an unrecognized species, please let me know :) {colorfont.colors.END}"
sucsessMessage = f"{colorfont.colors.SUCCSESS}Extract Succsess{colorfont.colors.END}"


def extracter(commands, parameters, AppName, ftype):
        
        
        osCommand = f"sudo {commands} {parameters} {AppName}{ftype}"
        
        try:
            subprocess.check_call(osCommand, shell=True)
            print(sucsessMessage)         
    
        except (OSError, subprocess.SubprocessError): 
            print(errorMessage)
    



            
                    
    


