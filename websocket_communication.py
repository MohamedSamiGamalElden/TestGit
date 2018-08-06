# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 16:25:47 2018

@author: Mohamed Gamaleldin
"""

#http://18.220.55.195/
#event : chat 

from socketIO_client import SocketIO, LoggingNamespace
import time, datetime


server1 ='http://127.0.0.1'
server2='18.220.55.195'
server3='ws://18.220.55.195'

port = 5000

def on_bbb_response(*args):
    print ('on_bbb_response', args)




with SocketIO(server3, port) as socketIO:
    socketIO.emit('message', "samy?",on_bbb_response)
    socketIO.wait(seconds=1)
    
