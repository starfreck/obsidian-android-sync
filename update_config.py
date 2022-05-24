#!/usr/bin/python3

import sys

print(sys.argv)

argv = sys.argv[1:]

remoteA = argv[0]
remoteB = argv[1]

with open("/storage/emulated/0/Documents/config.py", "rt") as file:
	x = file.read()
	
with open("/storage/emulated/0/Documents/config.py", "wt") as file:
    x = x.replace('remoteA = \"<<MUST SPECIFY>>\"',f'remoteA = "{remoteA}/"')
    x = x.replace('remoteB = \"<<MUST SPECIFY>>\"',f'remoteB = "{remoteB}"')
    file.write(x)