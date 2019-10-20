# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 23:46:09 2016

@author: giovanni
"""

header = '''
 <html>
    <head> 
        <title>%s</title>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=0;" />
        <meta name="apple-mobile-web-app-capable" content="yes" />
        <link rel="stylesheet" href="http://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.css" />
        <script src="http://code.jquery.com/jquery-1.11.1.min.js"></script>
        <script src="http://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js"></script>
    </head>
    <body>
'''

header_head ='''
    <div data-role='page' data-fullscreen="true" data-theme="c" >
    <div id='head' data-role='header' data-theme="b" data-add-back-btn="true" >
        <h5>
            %s
        </h5>
    </div>
'''

contentstr = '''
<div id ='content' data-role='content'>
'''

footer ='''
    </div>
         <div id ='footer' data-role='footer' data-theme="b" data-position='fixed'>
            <div id ='nav' data-role='navbar' >
                <ul>
                    <li><a href='/'>Home</a></li>
                    <li><a href='/downloads/'>Downloads</a></li>
                    <li><a href='/contact/'>Contact</a></li>
                    <li><a href='/about/'>About</a></li>
                </ul>
            </div>
        </div>
        <!-- End Page-->
        </div>
    </body>
</html>
'''

import cherrypy

class Page:
    title='default'    
    
    def header(self):
        return header%self.title
      
        
    def footer(self):
        return footer
        
index_content='''
<h1>Index Page</h1>
<p>
Here is some content for the index page<br>
Make sure you read this content throughly for this content is very important<br>
We want to be sure you understood this before you continue
</p>
<a href='/contact/'  class="ui-btn ui-btn-inline ui-icon-search ui-btn-icon-notext ui-corner-all ui-shadow ui-nodisc-icon ui-alt-icon" >Button</a>
'''
class IndexPage(Page):
    title='Index'
    
    def __init__(self):
        pass
    
    def index(self):
        yield self.header()
        yield header_head%self.title
        yield contentstr
        yield index_content
        yield self.footer()
    index.exposed=True
    

class AboutPage(Page):
    title = 'About'
    
    def index(self):
        yield self.header()
        yield header_head%self.title
        yield contentstr
        yield '''<h1>About</h1>'''
        yield self.footer()
    index.exposed =True
    
class ContactPage(Page):
    title = 'Contact'
    
    def index(self):
        yield self.header()
        yield header_head%self.title
        yield contentstr
        yield '''<h1>Contact</h1>'''
        yield self.footer()
    index.exposed =True

download_content='''
<h3>Downloads are for the masses</h3>
<p>These downloads are home grown apps<br>
Download them and use them at own risk.<br>
Don't come cryin' for me if something goes wrong.You can always aks for help<br>
But do this in a polite way and know that i am awfully busy so have a little patience with me
</p>

'''
class DownloadsPage(Page):
    title = 'Downloads'
    
    def index(self):
        yield self.header()
        yield header_head%self.title
        yield contentstr
        yield download_content
        yield self.footer()
    index.exposed =True
