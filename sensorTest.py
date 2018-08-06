# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 18:56:22 2018

@author: Mohamed Gamaleldin
"""

import csv
import pandas as pd

f = open('cleanSensors.csv', 'w')
writer = csv.writer(f,delimiter=',',lineterminator='\r') #writer is object, Here: declare write setting



with open("sensors.csv") as Ofile:
        reader = csv.reader(Ofile)
            
        for line in reader:
            if(line[2] == ''):
                continue    
            
            writer.writerow(line)
            print(line)
           
            
        f.close()