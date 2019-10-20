#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Dit moet de logwriter worden ik maak 'm eerst in de zandbak

Created on Mon Feb 29 12:13:33 2016
@author: giovanni
"""

import os

pics_path ='pictures'
logs_path = 'logs'

"""
Application Log

"""
class AppLog:
    #Applog init
    def __init__(self,logs):
        self.logs_path =logs
        self.name = self.__class__.__name__
        self.utils = Utils()
        #self.sendStdMesg(self.name)
        self.createLogPath()
        self.file_path = self.createFilePath()
        self.file_name = self.createFileName()
        self.file_location = self.locate(self.file_path)
    
    def createFilePath(self):
        cur_dir = os.getcwd()
        log_dir = cur_dir+"/"+self.logs_path
        return log_dir
        
    def createFileName(self):
        now  = self.utils.get_file_time()
        filename = ("Log.{}.log".format(now))
        return filename
    
    def createLogPath(self):
        if os.path.isdir(self.logs_path):
            return True
        else:
            os.mkdir(self.logs_path,777)
            print('Logs path created')
    
    def locate(self,log_dir):
        #utils = Utils()
    
        standard_log ="""
*******************************************************
Tournamant log started at {}
*******************************************************
"""
        location =log_dir+'/'+self.file_name
        if not os.path.isfile(location):
            file = open(location,'w')
            now = self.utils.get_human_time()
            
            file.write(standard_log.format(now))
            
            file.write('\n')
        else:
            pass
        
        return location
    
    def to_log(self,message):
        now = self.utils.get_unix_time()
        file = open(self.file_location,'a+')
        file.write("\n {}-{}".format(now,message))
        file.close()
        
    # sending a standard message
    def sendStdMesg(self,name):
        message ="""
***********************
Application {} log started
***********************
"""
        print(message.format(name))
                  
"""
Utils class
"""
class Utils:
    #Utils init
    def __init__(self):
        from time import gmtime,strftime
        self.gmtime = gmtime
        self.strftime = strftime
    #returning human readable time
    def get_human_time(self):
        timestmp = self.strftime("%A %d %B %r",self.gmtime())
        #human_time = self.strftime("%dd-%mm-%YYYY %H:%m:%s",self.gmtime())
        return timestmp# human_time 
    #returning mend to assist fielnaming convention
    def get_file_time(self):
        timestmp = self.strftime("%Y-%m-%d",self.gmtime())
        return timestmp
    # time mend to update database tables mysql format
    def get_unix_time(self):
        timestmp = self.strftime("%d-%m-%Y %I:%M:%S",self.gmtime())
        return timestmp          
#usage
# log = AppLog(logs_path)
# log.to_log("Document error no document found at location")
# log.to_log("SQLITE ERROR: no tables found with this name")
# log.to_log("SMTP ERROR: message could not be send to receiver")
