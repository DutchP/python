# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 19:31:02 2016

@author: giovanni
"""

constr=  dict() 

def showConstr(params):
    return ",".join(["%s:'%s'"%(key,value) for key,value in params.items()])
    
constr['server']='localhost'
constr['user']="user11"
constr['password']='$##@@87'

print(showConstr(constr))