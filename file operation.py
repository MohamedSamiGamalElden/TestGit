# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 14:46:47 2018

@author: Mohamed Gamaleldin
"""

file = open("test.txt","r+")
content=file.read()
content = content+"Hello\n"
file.write(content)
file.close()


"""    
    file = open("log.txt","r+")
    content=file.read()
    newcontent = content+ msg + "\n"
    file.write(newcontent)
    file.close()
"""
  