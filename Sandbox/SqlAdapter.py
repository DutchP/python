#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 20:57:39 2016

@author: giovanni
"""
import sqlite3 as lite
#==============================================================================
# SQL_Adapter class
#==============================================================================
class Adapter:
    #connection
    def __init__(self,db):
        self.connection = self.connect(db)
        
    def connect(self,db):
        try:
            connection = lite.connect(db)
            print("Succesfully connected")
            return connection
        except lite.Error as e:
            print("Something Went wrong\n%s"%e.args)
    
    def cursor(self):
        database = self.connection
        cursor = database.cursor()
        print("cursor assigned")
        return cursor
        
    def execute(self,sql):
        connection = self.connection
        cursor = self.cursor()
        try:
            if cursor.execute(sql):
                connection.commit()
                print("Script executed succesfully !!")
        except lite.Error as e :
            print("Oeps could not execute\n{}".format(e))
            
    def fetchall(self,sql):
        cursor = self.cursor()
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            return data
        except lite.Error:
            print("Could not fetch,Sorry")
    def fetchone(self,sql):
        cursor = self.cursor()
        try:
            cursor.execute(sql)
            data = cursor.fetchone()
            return data
        except lite.Error as e:
            print("Error: "+e)
        
        
#==============================================================================
# ObjAdapter
#==============================================================================
class ObjAdapter:
    
    def instantiate(self,record,parent):
         obj = parent
         reclen = len(record)
         for i in range(reclen):
            setattr(obj,obj.attrs[i],record[i])
         return obj
         
    def showSelf(self):
        tobj = self
        for key in self.attrs:
            value = getattr(self,key)
            tobj.key=value
            #print('{:16} : {:1}'.format(key,value))
        return tobj
            
         