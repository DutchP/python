# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 12:19:46 2016

@author: giovanni
"""

def application(env,start_response):
    start_response('200 OK',[('Content_Type','text/html')])
    return ["Hello!"]