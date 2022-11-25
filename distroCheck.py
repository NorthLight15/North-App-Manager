'''
Made for file checking
Python 3.10 Platform libary used.


'''



import os
import platform 

# Distro Check function
def Distro_check():
   
   platform_load =  platform.freedesktop_os_release()
   distro = platform_load["ID_LIKE"]
   distroUp = distro.upper()

   return distroUp