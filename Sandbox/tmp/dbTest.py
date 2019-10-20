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
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()
    
    print(data)
    con.close
    

if __name__=='__main__':
    Main()