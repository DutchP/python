# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 19:20:14 2016

@author: giovanni
"""
from threading import Thread 

def disp(par):    
    print(par)
objs=['join','me','at','the','beach']
par = '\n'.join(objs)# ["John","davis","robert","steel"]

r=Thread(target=disp(par))
r.start()
