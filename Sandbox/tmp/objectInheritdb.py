#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Met deze klasse bekijk ik het gebruik van inheritance op een 
geavanceerdere schaal
Created on Fri Jan 29 09:40:41 2016

@author: giovanni
"""
create_script = '''
CREATE TABLE users(id INT(6) PRIMARY KEY,
 naam varchar(40),voornaam varchar(80)
 )
'''
import sqlite3

class SQLIConnect:
    
    def __init__(self,db):
        self.connect(db)
        
    def connect(self,db):
        con = sqlite3.connect(db)
        return con
        
    def _execute(self,script):
        con = self
        cur = con.cursor()
        cur.execute(script)
        
    

class MyObject:
    
    def __init__(self):
        self.name
        self.first
        sqli = self.sqli = SQLIConnect("Mydb.db")
        sqli._execute(create_script)
    
    def _setName(self,name,first):
        self.name=name
        self.first=first
        
    def showMe(self):
        print("My name is %s %s"%(self.first,self.name))



class Person(MyObject):
    def __init__(self,name,first):
        self.name = name
        self.first =first
        

if __name__=='__main__':
    person = Person("Sparrow","Jack")
    person.showMe()