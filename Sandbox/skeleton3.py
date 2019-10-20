# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 23:46:09 2016

@author: giovanni
"""

header = '''
 <html>
    <head> 
        <title>Index for yield page</title>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=0;" />
        <meta name="viewport" content="width=device-width"/>
        <meta name="apple-mobile-web-app-capable" content="yes" />
        <link rel="stylesheet" href="http://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.css" />
        <script src="http://code.jquery.com/jquery-1.11.1.min.js"></script>
        <script src="http://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js"></script>
    </head>
    <body>
    <div id='head' data-role='header'  data-theme="a">
        <h5>
            Index page
        </h5>
    </div>
'''

nav = '''
<div id ='content' data-role='content'>
'''

footer ='''
    </div>
         <div id ='footer' data-role='footer' data-theme="a" data-position='fixed'>
            <div id ='nav' data-role='navbar' >
                <ul>
                    <li><a href='#'>Home</a></li>
                    <li><a href='#'>Downloads</a></li>
                    <li><a href='#'>Contact</a></li>
                    <li><a href='#'>About</a></li>
                
                </ul>
            </div>
        </div>
    </body>
</html>
'''

import cherrypy

class Page:
    
    def header(self):
        return header+nav
        
    def footer(self):
        return footer
        
    
class IndexPage(Page):
    
    def index(self):
        yield self.header()
        yield ''' This is content'''
        yield self.footer()
    index.exposed=True