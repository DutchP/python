#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 23:07:48 2016

@author: giovanni
"""

def showDict(*args):
    w = args[0]
    h = args[1]
    height =str(h)
    width =str(w)
    #printing ..    
    print("Width : {}\nHeight : {}".format(width,height))
    
    
cords = dict({'width':23,'height':12})

showDict(23,12)