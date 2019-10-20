# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 18:18:18 2016

@author: giovanni
"""
import cherrypy

from Pages import Page

class IndexPage(Page):
    title = 'Ajax Test'
    
    def index(self):
        return '''
        
        
        '''
    index.exposed=True
    
    def answer(self):
        return '''
        
        
        '''
    answer.exsposed=True


if __name__=='__main__':
    config={
        '/':{
            'tools.staticdir.root':'/home/giovanni/bin/web/sandbox/'
        },
        '/static':{
            'tools.staticdir.on':True,
            'tools.staticdir.dir':'public'
        },
        '/css':{
            'tools.staticdir.on':True,
            'tools.staticdir.dir':'./css'
        },
        '/images':{
            'tools.staticdir.on':True,
            'tools.staticdir.dir':'./images'
        },
        '/js':{
            'tools.staticdir.on':True,
            'tools.staticdir.dir':'./js'
        }
    }
    
    mywsgiapp = cherrypy.Application(IndexPage(),'/',config=config)
    cherrypy.tree.graft(mywsgiapp,'/')
    #creating server bit
    cherrypy.server.unsubscribe()
    server = cherrypy._cpserver.Server()
    #configuring the server object
    server.socket_host ="0.0.0.0"
    server.socket_port = 8080
    server.thread_pool = 30
    server.subscribe()
    #starting the Server
    print("Starting Server")
    cherrypy.engine.start()
    cherrypy.engine.block()