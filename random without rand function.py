# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 02:04:02 2018

@author: Mohamed Gamaleldin
"""
""" it's also possible to generate random number using, Linear Feedback shift Register """

import time
r=5

while 1:
    
    r = ((r * 7621) + 1) % 32768;
    print(r)
    time.sleep(1)
