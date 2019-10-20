# -*- coding: utf-8 -*-
import hashlib

"""
Created on Thu Feb 11 18:41:44 2016

@author: giovanni
"""

def showString(params):
    return ",".join(["%s='%s'" % (key, value) for key, value in params.items()])
    
'''
myParams = {"server":"mpilgrim", \
				"database":"master", \
				"uid":"sa", \
				"pwd":"secret"
				}
'''

connection_details ={"server":"localhost","user":"toor","password":hashlib.md5().update("@hgk%4").hexdigest()} 
#{"server":"localhost","ipadres":"127.0.0.1","user":"toor","password":"@hgk%4"}
print (showString(connection_details))
