# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 15:14:46 2016

@author: giovanni
"""

import cherrypy


class SecondPage:
    
    def index(self):
        return '''
        <h1>This is Second Page </h1>
        '''
    index.exposed = True

class IndexPage:
    
    def __init__(self):
       self.secondPage = SecondPage()
    
    @cherrypy.expose
    def index(self):
        return open("index.html")
        
    @cherrypy.expose
    def NameAccept(self,name):
        return '''
            name is %s
        '''%name
        
    @cherrypy.expose
    def MakeFile(self):
        return '''
        <p>
        U hebt een goeie keuze gemaakt..
        ga nu verder<br>
        Volg deze <a href="/LevelTwo">link<a/>
        </p>
        <a href="./secondPage">link<a/>
        <p>[<a href="../">Return</a>]</p>
        '''
        
    @cherrypy.expose
    def LevelTwo(self):
        return open("level2.html")
        
    @cherrypy.expose
    def AnswertoTwo(self,name):
        return '''
        <p>
        Je bent geslaagd %s!!!
        </p>
        '''%name
        
    def tick(self):
        return "<a href='./sp/'>link</a>" 
    tick.exposed =True