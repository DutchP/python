#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 09:37:28 2016

@author: giovanni
"""
import sqlite3

def Main():
    """Connecting to a new database"""
    connection = sqlite3.connect('testdb.db')
    #creating a cursor to maintain the connection
    cursor = connection.cursor()
    #In dbQuery we've entered information to the database
    #Now let's try to read it
    #Read function
    cursor.execute('SELECT * FROM exotische_dieren')    
    data  = cursor.fetchall()
    print("\nEen lijst van Exotische diersoorten\n")
    print("Id\tNaam van dier")
    print("-"*40)
    for row in data:
        print('\033[0m',row[0],"\t",row[1])
    #print(data)
    connection.close
    print("\n")

if __name__=='__main__':
    Main()