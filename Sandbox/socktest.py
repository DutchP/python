# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 17:20:18 2016

@author: giovanni
"""

import socket

host_name = socket.gethostname()
print(host_name)
ipadr = socket.gethostbyname(host_name)
print(ipadr)
outip = socket.gethostbyaddr(ipadr)
print(outip)
#outerip = socket.getnameinfo(host_name)
#print(outerip)