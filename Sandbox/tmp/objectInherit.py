#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Met deze klasse bekijk ik het gebruik van inheritance op een 
geavanceerdere schaal
Created on Fri Jan 29 09:40:41 2016

@author: giovanni
"""

class MyObject:
    def __init__(self):
        self.name
    
    def _setName(self,name):
        self.name=name
        
    def showMe(self):
        print("My name is "+self.name)

class Person(MyObject):
    def __init__(self,name):
        self.name = name
        

if __name__=='__main__':
    person = Person("Jack")
    person.showMe()