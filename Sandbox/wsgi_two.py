
HELLO_WORLD='''
<!DOCTYPE html>
<html>
    <head> 
        <title>NeeltjesPlek</title>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=0;" />
        <meta name="apple-mobile-web-app-capable" content="yes" />
        <link rel="stylesheet" href="http://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.css"  />
        <link rel="stylesheet" href="/css/custom.css"/>
        <script src="http://code.jquery.com/jquery-1.11.1.min.js"></script>
        <script src="http://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js"></script>
    </head>
    <body>
        <!-- ### Page1 ## -->
        <div id='index' data-role='page' class="ui-page" data-title="Index">
            <!--<header data-role='header' data-theme="b" data-add-back-btn="true"></header>-->
            <div data-role='content'>
                <h1>Neeltjes Plek</h1>
                <div class="homeMenu">
                    <a class="glyphishIcon" href="/#contact" 
                    data-role="button" data-icon="location"
                    data-inline="true" data-iconpos="top">
                    Contact
                    </a>
                    <a class="glyphishIcon flike" href="https://touch.facebook.com/IrmanCreatief" 
                    data-role="button" data-icon="flike" data-iconpos="top" data-inline="true">
                    Like ons
                    </a>
                    <a class="glyphishIcon products" data-role="button" data-inline="true" data-icon="flike"
                    data-iconpos="top" href="#about">
                    Ons Hoekje
                    </a>
                </div>
                <div id="pageinfo" data-theme="a" ><p><h3>Welkom</h3> Bij Irma Creatief<br>Wij hebben enkele leuke goederen in de aanbieding.<br>Neem even een kijkje in de hoek </p></div>
            </div>
            <footer data-role='footer' data-position='fixed'> <h2>footer</h2> </footer>
        </div>
        <!-- ### Page2 ## -->
        <div id='about' data-role='page' class="ui-page" data-title="Over Neeltje">
            <header data-role='header' data-theme="b" data-add-back-btn="true"><h1>Over Neeltje</h1></header>
            <div data-role='content'>
                
                <div id='mypoll'>
                
                </div>
                <div id="page2info" data-theme="b">
                    <p>We hebben onder andere de volgend categorieën </p>
                </div>
            </div>
            <div id='footer' data-role='footer' data-position='fixed'> 
                <div id='nav' data-role="navbar">
                    <ul>
                    <li><a href="/" >Home</a></li>
                     <li><a href="./#contact">Contact</a></li>
                    <li><a href="./#about" class="ui-btn-active ui-state-presist">Over</a></li>
                    <li><a href="./#producten">Producten</a></li>
                    </ul>
                </div> 
            </div>
        </div>
        <!-- ### Page3 ## -->
        <div id='contact' data-role='page' class="ui-page" data-title="Contacten">
            <header data-role='header' data-theme="b" data-add-back-btn="true"><h1>Contact</h1></header>
            <div data-role='content' >
                <a href="tel:+31644457158" class="ui-btn ui-btn-icon-top ui-btn-inline">Bel</a>
                <a href="sms:+31644457158" class="ui-btn ui-btn-icon-top ui-btn-inline">Sms</a>
                <a href="mail:neeltje38@gmail.com" class="ui-btn ui-btn-icon-top ui-btn-inline">Mail</a>
                <p><b>Of kom gerust langs op:</b></p>
                <div>
                <a href="https://maps.google.com/maps?q=Nigellestraat+87,+1032+BL+Amsterdam&hl=nl&sll=52.396712,4.9108241,16z=9771+N+Nigellestraat+87,+1032+BL+Amsterdam/@52.396712,4.9108241,16z"><img />
                    <img src="http://maps.googleapis.com/maps/api/staticmap?center=Nigellestraat+87,+1032+BL+Amsterdam&zoom=13&size=200x200&scale=2&maptype=roadmap&markers=label:H%7CNigellestraat+87,+1032+BL+Amsterdam&sensor=true"/>                
                </a>
                </div>
            </div>
            <div id='footer' data-role='footer' data-position='fixed'> 
                <div id='nav' data-role="navbar">
                    <ul>
                    <li><a href="/" >Home</a></li>
                    <li><a href="./#contact" class="ui-btn-active ui-state-presist">Contact</a></li>
                    <li><a href="./#about">Over</a></li>
                    <li><a href="./#producten">Producten</a></li>
                    </ul>
                </div> 
            </div>
        </div>
        <!-- ### Page4 ## -->
        <div id='producten' data-role='page' class="ui-page" data-title="Producten">
            <header data-role='header' data-theme="b" data-add-back-btn="true"><h1>Producten</h1></header>
            <div data-role='content' >
                <div id="pageinfo" data-theme="a" ><h3>Producten</h3><p>Zijn tevreden dingen die overal voor gebruikt kunnen worden</p></div>
                
            </div>
            <div id='footer' data-role='footer' data-position='fixed'> 
                <div id='nav' data-role="navbar">
                    <ul>
                    <li><a href="/" >Home</a></li>
                    <li><a href="./#contact">Contact</a></li>
                    <li><a href="./#about">Over</a></li>
                    <li><a href="./#producten" class="ui-btn-active ui-state-presist">Producten</a></li>
                    </ul>
                </div> 
            </div>
        </div>
    </body>
</html>
<script type='text/javascript'>
;(function($){
    $.fn.about = function(){
        $("<h1/>",{
            text:"Over Neeltje"        
        }).appendTo(this)
        var ul = $("<ul data-role='listview' data-inset='true'/>")
        var x, y, categories=['About','Contact','Producten'];
        var urls = ['./#about','./#contact',./#producten']
        for(x=0,y=categories.length;x<y;x++){
            var li = $("<li/>")
            $("<a/>",{
                text:categories[x],
                href:urls[x]
            }).appendTo(li)            
            li.appendTo(ul)
        }            
        ul.appendTo(this)
    }
 }(jQuery));
</script>
<script type='text/javascript'>
$(function(){
    $('#mypoll').about()
})
</script>
'''
import cherrypy

class WebApp(object):
    
    
    def index(self):
        return HELLO_WORLD
    index.exposed=True
    
    def vazen(self):
        return '''<H1>Vazen</H1>'''
    

def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html;charset=utf-8')]
    start_response(status, response_headers)
    return HELLO_WORLD

if __name__=='__main__':
    
    config ={
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
        }
    }    

    wsgiapp = cherrypy.Application(WebApp(),'/',config=config)    
    vhost = cherrypy._cpwsgi.VirtualHost(application)
    cherrypy.tree.graft(wsgiapp,'/')
    #cherrypy.tree.graft(application,"/")
    cherrypy.server.unsubscribe()
    server = cherrypy._cpserver.Server()
    
    #configuring the server object
    server.socket_host ="0.0.0.0"
    server.socket_port = 8080
    server.thread_pool = 30
    
    server.subscribe()
    
    cherrypy.engine.start()
    cherrypy.engine.block()
