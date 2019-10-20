#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 22:37:53 2016

@author: giovanni
"""
import sqlite3 as sqlite

class SqliObj:
    #connection
    def __init__(self,db):
        self.connection = self.connect(db)
        
    def connect(self,db):
        try:
            connection = sqlite.connect(db)
            print("Succesfully connected")
            return connection
        except sqlite.Error as e:
            print("Something Went wrong\n%s"%e.args)
    
    def cursor(self):
        database = self.connection
        cursor = database.cursor()
        print("cursor assigned")
        return cursor
        
    def execSql(self,sql):
        connection = self.connection
        cursor = self.cursor()
        try:
            if cursor.execute(sql):
                connection.commit()
                print("Script executed succesfully !!")
        except sqlite.Error:
            print("Oeps could not execute\n")
            
    def fetchall(self,sql):
        cursor = self.cursor()
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            return data
        except sqlite.Error:
            print("Could not fetch,Sorry")
    def fetchone(self,sql):
        cursor = self.cursor()
        try:
            cursor.execute(sql)
            data = cursor.fetchone()
            return data
        except sqlite.Error:
            print("Oops")
            
db = SqliObj("database/local.db")

#class ObjectAdapater:
#    def __init__(self):
#cursor = db.cursor()
#insert_script = "INSERT INTO users VALUES(null,'{}','{}','{}')".format('Carol','Mayfield','CarMay@holland.de')
#db.execSql(insert_script)
#select_script = "SELECT * FROM users ORDER BY naam ASC"
#users = db.fetchall(select_script)
#for user in users:
    #print(user)
