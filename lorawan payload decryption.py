# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 00:28:31 2018

@author: Mohamed Gamaleldin
"""


from lora.crypto import loramac_decrypt
import binascii


# actual 23A5 
payload = 'B148A134' #32 hex


sequence_counter = 0x6002

key = 'AFBECD56473829100192837465FAEBDC'

dev_addr = '001B3109'

data= loramac_decrypt(payload, sequence_counter,key,dev_addr)


print(data)


