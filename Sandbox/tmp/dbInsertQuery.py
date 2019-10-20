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
    # We can now enter more information into the table
    """cur.execute('''CREATE TABLE exotische_dieren
             (id INTEGER PRIMARY KEY,
              namen varchar(40) NOT NULL,
              leefomgeving varchar(128) )''')"""
              
    cur.execute('INSERT INTO exotische_dieren VALUES(null,"beer","")')
    cur.execute('INSERT INTO exotische_dieren VALUES(null,"tijger","")')
    cur.execute('INSERT INTO exotische_dieren VALUES(null,"poema","")')
    cur.execute('INSERT INTO exotische_dieren VALUES(null,"leeuw","")')
    cur.execute('INSERT INTO exotische_dieren VALUES(null,"olifant","")')
    con.commit()
    con.close
    
if __name__=='__main__':
    Main()