#!/usr/bin/env python3

import os
import sys

Color_Off='\033[0m'       # Text Reset
Green='\033[0;32m'        # Green
Cyan='\033[0;36m'         # Cyan
Red='\033[0;31m'          # Red

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

site = input(Color_Off + "Ingrese el sitio a bloquear: " + Green)

while site.isspace() or len(site) <= 1:
	print (Red + "ERROR Ingrese una URL o SITIO correcto")
	site = input(Color_Off + "Ingrese el sitio a bloquear: ")

with open(hosts_path, 'r+') as file:
	content = file.read()
	if site in content:
		pass
	else:
		file.write(redirect+"\t"+site+"\n")

print (Cyan + "Sitio Agregado correctamente :)")