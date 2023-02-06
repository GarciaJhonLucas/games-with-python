#!/usr/bin/env python3 Clau@170398.A
from pytube import YouTube
import os
import sys
from colorama import Fore, Back, Style

Color_Off="\033[0m"       # Text Reset
Green="\033[0;32m"        # Green
Cyan="\033[0;36m"# Cyan
Red="\033[0;31m"          # Red
url = input(f"Enter your youtube url: " + Fore.RED)

while url.isspace() or len(url) <= 1:
	print (f"{Red}ERROR Ingrese una URL")
	url = input(f"{Color_Off}Enter your youtube url: ")

yt = YouTube(url)

print(f"{Cyan}=================================={Color_Off}")
print(f"Titulo .........: {Green}{yt.title}{Color_Off}")
print(f"Duracion (seg)..: {Green} {str(yt.length)} {Color_Off}")
print(f"{Cyan}=================================={Color_Off}")

option = input("Audio: A | Video V | Salir X: ")

while option.isspace():
	print (Red + "ERROR Ingrese una OPCION")
	option = input(f"{Color_Off}Audio: A | Video V | Salir X: {Red}")

if option.upper() == "X":
    sys.exit(0)
if option.upper() == "A":
    stream = yt.streams.get_by_itag("251")
else:
	stream = yt.streams.get_highest_resolution()

stream.download(os.path.expanduser('~/Downloads'))
print (Cyan + "=======================" + Color_Off)
print (Cyan + "downloaded successfully" + Color_Off)
