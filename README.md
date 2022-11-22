# North-App-Manager

Simple application and source file download manager for Linux users

![Beta Version](https://img.shields.io/badge/Version-Beta-F05032?style=for-the-badge&logo=github)

# What Does It Do?

Linux distributions are operating systems that takes some time for standard users to get used to. Linux application managers are softwares that makes downloading applications from their main source easy for everyone to use. This program is yet another source manager.

## Fast and Reliable

North App Manager is primarily open source software, all sources are taken from AppSources/sources.yaml and all downloads provided from original manufacturer sources.

## How Does It Work?

Firstly, it searches for the file you specified with local package managers, if they cannot find the specified package then it looks at its own sources, and if there is a match, it downloads and extracts the files for you.

# How To Use

## Requirements

![Python 3.10](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)

## Installation

Be sure you have git on your system.

```sh
sudo apt install git		# On Debian
sudo pacman -S git			# On Arch Linux
sudo dnf install git 		# On Fedora
sudo zypper in git			# On OpenSuse
sudo emerge --ask git		# On Gentoo
sudo xbps-install xtools 	# On Void Linux
```

Then you can clone this repository and run the program:
```sh
git clone https://github.com/NorthLight15/North-App-Manager.git
cd North-App-Manager/
./NorthAppManager.py
```

**or just** download [North App Manager ZIP file](https://github.com/NorthLight15/North-App-Manager/archive/refs/heads/main.zip), extract it and run the app with the command below:

```sh
 ./NorthAppManager.py
```
