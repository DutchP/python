# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 18:35:41 2016

@author: giovanni
"""

headerStr='''
<!DOCTYPE html>
<html>
    <head> 
        <title>%s</title>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=0;" />
        <meta name="apple-mobile-web-app-capable" content="yes" />
        <link rel="stylesheet" href="http://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.css"  />
        <link rel="stylesheet" href="/css/custom.css"/>
        <script src="http://code.jquery.com/jquery-1.11.1.min.js"></script>
        <script src="http://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js"></script>
    </head>
    <body>
'''

footerStr='''
        </body>
</html>
<script src="/js/custom.js"></script>
<script>
$(function(){
    $("#send").click(function(){
        generateData()    
    })
})
</script>
'''

IndexStr='''
        <div id='contact' data-role='page' class="ui-page" data-title="Index Page">
            <header data-role='header' data-theme="b" data-add-back-btn="true"><h1>Contact</h1></header>
            <div data-role='content' >
                <a href='answer' class="ui-btn ui-btn-inline ui-icon-search ui-btn-icon-notext ui-corner-all ui-shadow ui-nodisc-icon ui-alt-icon" >Button</a>
                
                <!-- cancled out -->         
                <!-- <a href="tel:+31644457158" class="ui-btn ui-btn-icon-top ui-btn-inline">Bel</a>
                <a href="sms:+31644457158" class="ui-btn ui-btn-icon-top ui-btn-inline">Sms</a>
                <a href="mail:neeltje38@gmail.com" class="ui-btn ui-btn-icon-top ui-btn-inline">Mail</a>
                <p><b>Of kom gerust langs op:</b></p>
                <div>
                <a href="https://maps.google.com/maps?q=Nigellestraat+87,+1032+BL+Amsterdam&hl=nl&sll=52.396712,4.9108241,16z=9771+N+Nigellestraat+87,+1032+BL+Amsterdam/@52.396712,4.9108241,16z"><img />
                    <img src="http://maps.googleapis.com/maps/api/staticmap?center=Nigellestraat+87,+1032+BL+Amsterdam&zoom=13&size=200x200&scale=2&maptype=roadmap&markers=label:H%7CNigellestraat+87,+1032+BL+Amsterdam&sensor=true"/>                
                </a> -->
                <!-- End --cancled out -->
               
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
'''

AnswerStr='''
      <div id='contact' data-role='page' class="ui-page" data-title="Answer">
            <header data-role='header' data-theme="b" data-add-back-btn="true"><h1>Answer</h1></header><div>
            <div data-role='content' >
            <button id="send" data-inline='true'>Send</button>
                <div id='placeholder'>
                    
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
'''

