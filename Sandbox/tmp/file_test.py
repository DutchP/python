#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This is a program to test file reading
Created on Wed Jan  6 21:32:33 2016

@author: giovanni
"""
from __future__ import print_function

f = open("MyText.txt",'r')
#firstline = f.readline()
#print(firstline)
for line in f:
    print(line,end ='')

f.close()