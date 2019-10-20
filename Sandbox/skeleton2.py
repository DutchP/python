# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 19:47:51 2016

@author: giovanni
"""

class Page:
    
    def header(self):
        return '''
        <html>
            <head> <title>Index page</title></head>
            <body>
        '''
        
    def footer(self):
        return '''
            </body>
            
        </html>
        '''
        
        
class IndexPage(Page):
    def __init__(self):
        self.secondPage = SecondPage()
    
    def index(self):
        yield self.header()
        yield '''
        <h1>First Page</h1>
        <a href="./secondPage">Go to the second page</a>
        '''
        yield self.footer()
    index.exposed = True
    
    
class SecondPage(Page):
    def index(self):
        yield self.header()
        yield '''
        <h1>Second Page</h1>
        [<a href="../">back</a>]
        '''
        yield self.footer()
    index.exposed = True        
    