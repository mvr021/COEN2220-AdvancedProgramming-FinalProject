# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 11:53:01 2021

@author: yeya
"""

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

import time
from abc import ABC, abstractmethod
from multipledispatch import dispatch

class base(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def ex(self):
        pass
    

class aplicacion(base):
    
    def __init__(self,x):
        self.x = x
    
    def ex(self):
        
        #execute the program
        exec(compile(open( self.x , "rb").read(), self.x, 'exec'))
 
        
class stats(object):
    stattext = "Runtime:"
    def __init__(self,y,message,signature):
        self.y = y
        self.message = message
        self.signature = signature
       
    @classmethod
    @dispatch(type,str)
    def operacion(cls,y):     
        
    #compute the time of execution
        start = time.time()
        Obj1 = aplicacion('aplicacion.py' )
        Obj1.ex()
        
        end = time.time()
        print("\n",y, end-start)
    
    @classmethod
    @dispatch(type,str,str)
    def operacion(cls,message,signature):
        
        #print final message
        print("\n",message,signature)
    
print("\n",stats.stattext)
stat = stats.operacion("The time of execution of this program is :")
stat = stats.operacion("Thank you for using this program ","-Mireya Vázquez")
