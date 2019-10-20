#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 22:03:20 2016

@author: giovanni
"""

from threading import Thread
from queue import  Queue
from time import sleep


def runMe():
    guiQueue = Queue()
    
    #print('I am in a thread')
    for idx in range(11):
        sleep(1)
        print(guiQueue)
        guiQueue.put('I am within a que /'+str(idx))
        print(guiQueue.get())
    
runT = Thread(target=runMe)
runT.start()