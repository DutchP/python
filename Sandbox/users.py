#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Deze class importeerd en gebruikt de database class
Created on Sat Jan 30 16:58:46 2016

@author: giovanni
"""

#from database.py import SqliObj as database
from database import  *
#import sqlite3 as sqlite

class User:
    def __init__(self):
        self.table = "users"
        self.dbfields =['id','name','first','email','desc']
        
        
    def create_table(self):
        sql = "CREATE TABLE users(id INTEGER PRIMARY KEY, name VARCHAR(50),first VARCHAR(50),email VARCHAR(128),desc TEXT)"
        try:
            db.execSql(sql)
            print("table succesfully created")
        except sqlite.Error :
            print('Failed to connect to DB')
            
    def userInsert(self,row=[]):
        sql="INSERT INTO users VALUES(null,'%s','%s','%s','%s')" %(row[1],row[2],row[3],row[4])
        db.execSql(sql)        
     
    def fetchAll(self):
       sql="SELECT * FROM users ORDER BY id  ASC"
       data = db.fetchall(sql)
       return data
       
    def fetchOne(self, _id):
        _obId =int(_id)
        sql  ="SELECT * FROM users WHERE id='%d'"%(_obId)
        data = db.fetchone(sql)
        return data
    
row4 = ['','Patrick','Darryl','','Dit is een hoofdgebruiker']
#userInsert()
user = User()
row0 = ['','henk','Arron','','']
row1=  ['','lucas','Deventer','','']
row2 = ['','Piet','Schrijvers','pietniet@gmail.net','']
row3 = ['','Sara','Siomara','alive@live.nl','Dit is een beschrijving van de gebruiker']
#user.create_table()
#user.userInsert(row4)
#user.userInsert(row3)
users = user.fetchAll()
singleU = user.fetchOne('5')


for user in users:
    print(user)
print("="*30)
print(singleU)