#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Ik hoop met dit programma meer grip te krijgen op mijn 
program flow.
-----------------------------------------------------------
Dit programma accepteerd een integer als argument
Ik heb nog niet bepaald wat met dit getal gaat gebeuren 
maar, er wordt in ieder geval een exceptie opgegooid als er 
geen getal is ingevoerd.
We gaan van daaruit verder..
-----------------------------------------------------------
Created on mon 4 januari 13:58:30 2016
@author: giovanni
"""
__version__ ="01"
__name__ = "User inerface one"

import subprocess,sys
args = sys.argv
ln = len(args)

def call_doc():
    subprocess.call("clear")
    print ("\n"*30)
    print (__doc__)
    print ("*"*40)
    print ("Om dit programma te gebruiken")
    print("Dien je een getal als argument mee te geven")
    print("ex:\nnum_drive.py 1 (\"print the table\")\nnum_drive.py 2 (\"print another table\")")
    print ("*"*40)
    


if ln == 1:
    call_doc()
else:
    subprocess.call("clear")
    num = sys.argv[1]
    try:
        int(num)
        if(int(num)==1):
            print("1 is het begin")
        elif(int(num)==2):
            print("2 is twee keuzes")
        else:
            print("Probeer 1 of 2 ")
    except ValueError:
        print("Sorry u dient een cijfer in te vullen")