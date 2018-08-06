# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 03:33:11 2018

@author: Mohamed Gamaleldin
"""

from socketIO_client import SocketIO, BaseNamespace

server2='18.220.55.195'
server3='ws://18.220.55.195'



def on_connect():
    print('connect')

def on_disconnect():
    print('disconnect')

def on_reconnect():
    print('reconnect')

def on_aaa_response(*args):
    print('on_aaa_response', args)

socketIO = SocketIO(server3, 5000, LoggingNamespace)
socketIO.on('connect', on_connect)
socketIO.on('disconnect', on_disconnect)
socketIO.on('reconnect', on_reconnect)

# Listen
socketIO.on('aaa_response', on_aaa_response)
socketIO.emit('aaa')
socketIO.emit('aaa')
socketIO.wait(seconds=1)

# Stop listening
socketIO.off('aaa_response')
socketIO.emit('aaa')
socketIO.wait(seconds=1)

# Listen only once
socketIO.once('aaa_response', on_aaa_response)
socketIO.emit('aaa')  # Activate aaa_response
socketIO.emit('aaa')  # Ignore
socketIO.wait(seconds=1)