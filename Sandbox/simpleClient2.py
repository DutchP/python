#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 00:19:22 2016

@author: giovanni
"""

import socket

s = socket.socket()
 #host = socket.gethostbyaddr('raspberrypi')
port = 2100
s.connect(('192.168.1.101',port))
print (s.recv(1024))
s.close()
