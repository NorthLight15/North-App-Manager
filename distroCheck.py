import os
import platform 


def Distro_check():
   
   platform_load =  platform.freedesktop_os_release()
   distro = platform_load["ID_LIKE"]
   distroUp = distro.upper()

   return distroUp