# -*- coding: utf-8 -*-
"""

Created on Thu Jan  7 01:19:27 2016
@author: giovanni
"""
import sqlite3

class SQLITEBrowser():
    """ This class is the base to the sqlite operations"""
    def __init__(self):
        self.dbname = 'testdb.db'
        self.connection = self.connect(self.dbname)
    """Creates the Object as the connection"""
    def connect(self,dbname):
        connection = sqlite3.connect(self.dbname)
        return connection
    """Closes the connection"""
    def close_connection(self):
        self.connection.close()
    """Executes the sql given to the object"""
    def execute_sql(self,sql,items):
        cursor = self.connection.cursor()
        cursor.execute(sql,items)
        self.connection.commit()
        self.close_connection()
        
        
if __name__=='__main__':
    sqli = SQLITEBrowser()
    obname ="orangoetan"
    obplc= ""
    sqli.execute_sql('INSERT INTO exotische_dieren VALUES(null,?,?)',(obname,obplc))