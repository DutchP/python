#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 09:37:28 2016

@author: giovanni
"""
import sqlite3

def Main():
    """Connecting to a new database"""
    con = sqlite3.connect('testdb.db')
    #creating a cursor to maintain the connection
    cur = con.cursor()
    #No were going to try to Create a table in the sqlite database
    #Create function
    cur.execute('CREATE TABLE dieren(id INT,namen TEXT)')
    cur.execute('INSERT INTO dieren VALUES(1,"aap")')
    cur.execute('INSERT INTO dieren VALUES(2,"hond")')
    cur.execute('INSERT INTO dieren VALUES(1,"kat")')
    con.commit()
    
    
    #print(data)
    con.close
    

if __name__=='__main__':
    Main()