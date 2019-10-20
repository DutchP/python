# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 16:12:10 2016
"""
__author__ = " Giovanni Herdigein"
__version__= "1"

from os import getcwd
import os
import sqlite3 as lite
#==============================================================================
# Main class
#==============================================================================
class Main():
    
    def __init__(self):
        self.name = self.__class__.__name__
        self.filename = os.path.basename(__file__ )
        self.cur_dir = getcwd()
        self.dbName= self.createDbDir()
        defaultdb = "localdb.db"
        self.db =self.createDbFile(defaultdb)
        
        
    def showName(self):
        print("Class name: "+self.name)
        print("File Directory : "+self.cur_dir)
        print("File name: "+self.filename);
        print("Local db file : "+self.db)

    def createDbDir(self):
        if os.path.isdir("database"):
            pass
        else:
            os.mkdir("database")
        return "database"
    
    def createDbFile(self,defaultdb):
        localfile = "{}/{}/{}".format(self.cur_dir,self.dbName,defaultdb)
        #localfile =self.cur_dir+"/database/"+"localdb.db"
        if os.path.isfile(localfile):
            pass
        else:
            self.openfile(localfile)
        return localfile
         
    def openfile(self,filename):
        try:
            lite.connect(filename)
            print("sqlite db created")
        except lite.Error as e:
            print("Could not open database file\n{}".format(e))
            
#==============================================================================
# running the  app
#==============================================================================
def run_App():
    if __name__=='__main__':
       Main()
        #main.showName()
        
global base_path 
base_path = 'null'
print("base_path : "+ base_path)

if not os.path.isfile(base_path):
    main = Main();
    base_path = main.db
    
run_App()
print(base_path)

#db = SQL_Adapter(base_path)
from Tournament import Tournament

tournament = Tournament()
tournament.insertTournament("Default Tournament 3")
