#!/usr/bin/env python
from pytube import YouTube
import os
import sys

Color_Off='\033[0m'       # Text Reset
Green='\033[0;32m'        # Green
Cyan='\033[0;36m'         # Cyan
Red='\033[0;31m'          # Red

url = input("Enter your youtube url: ")

while url.isspace() or len(url) <= 1:
	print (Red + "ERROR Ingrese una URL")
	url = input(Color_Off+"Enter your youtube url: ")

yt = YouTube(url)

print (Cyan + "==================================" + Color_Off)
print("Titulo .........: " + Green + yt.title + Color_Off)
print("Duracion (seg)..: " + Green + str(yt.length) + Color_Off)
print (Cyan + "==================================" + Color_Off)

option = input("Audio: A | Video V | Salir X: ")

while option.isspace() or len(option) <= 1:
	print (Red + "ERROR Ingrese una OPCION")
	option = input("Audio: A | Video V: ")

if option.upper() == "X":
    sys.exit(0)
if option.upper() == "A":
    stream = yt.streams.get_by_itag("251")
else:
	stream = yt.streams.get_highest_resolution()

stream.download(os.path.expanduser('~/Downloads'))
print (Cyan + "downloaded successfully" + Color_Off)