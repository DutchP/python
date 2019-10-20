# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 18:18:18 2016

@author: giovanni
"""
import cherrypy

from Pages import Page
import WebString

class IndexPage(Page):
    title = 'Ajax Test'
    
    def index(self):
        yield self.header()
        yield WebString.IndexStr
        yield self.footer()
    index.exposed=True
    
    def answer(self):
        yield self.header()
        yield WebString.AnswerStr
        yield self.footer()
    answer.exposed=True
    
    def generate(self,name=None):
        
        def showfield():
            for i in range(5):
                yield "<li><a href=''>prijs=%s"%(str(i))+"</a></li>"
        return showfield()
        
    generate.exposed=True


if __name__=='__main__':
    config={
        '/':{
            'tools.staticdir.root':'/storage/extSdCard/scripts/sandbox/'
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
    server.socket_port = 8081
    server.thread_pool = 30
    server.subscribe()
    #starting the Server
    print("Starting Server")
    cherrypy.engine.start()
    cherrypy.engine.block()