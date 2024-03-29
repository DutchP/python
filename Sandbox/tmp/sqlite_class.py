#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
DROP TABLE IF EXISTS Cars;

'''
import sqlite3 as sqlite
import sys

try:
    con = sqlite.connect('test.db')

    cur = con.cursor()  

    cur.executescript("""
        CREATE TABLE Cars(id INTEGER PRIMARY KEY, name TEXT, number INT);
        INSERT INTO Cars VALUES(1,'Audi',52642);
        INSERT INTO Cars VALUES(2,'Mercedes',57127);
        INSERT INTO Cars VALUES(3,'Skoda',9000);
        INSERT INTO Cars VALUES(4,'Volvo',29000);
        INSERT INTO Cars VALUES(5,'Bentley',350000);
        INSERT INTO Cars VALUES(6,'Citroen',21000);
        INSERT INTO Cars VALUES(7,'Hummer',41400);
        INSERT INTO Cars VALUES(8,'Volkswagen',21600);
        """)

    con.commit()
    
except sqlite.Error, e:
    
    if con:
        con.rollback()
        
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close() 