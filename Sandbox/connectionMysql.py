#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Database connection to the mysql server
Created on Sun Feb 14 21:27:23 2016
@author: giovanni
"""
import mysql.connector as mysql
import GuiDBConfig as guiConf

conn = mysql.connect(**guiConf.dbConfig)
print(conn)

