# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 16:40:03 2018

@author: Mohamed Gamaleldin
"""


from lora.crypto import loramac_decrypt


frame=b"4009311B000041031E5C3EC56B424A"
key = 'AFBECD56473829100192837465FAEBDC'


#original payload = 100 5809
#python upper bound is exclude d
MHDR=frame[0:2]

#bytes
_DevAddr=frame[2:10]

#list
DevAddr=bytearray()

for i in range(len(_DevAddr),0, -2):
    DevAddr.extend(_DevAddr[i-2:i])

bDevAddr=bytes(_DevAddr)
   
SDevAddr=DevAddr.decode(encoding="utf-8")

FCTR=frame[10:12]

FCNT=frame[14:16]+frame[12:14]

FPORT=frame[16:18]

Payload = frame[18:-8]

MIC= frame[-8:]

data= loramac_decrypt(Payload,int(FCNT,16),key,SDevAddr)

hexData =""
for x in data:
    if(x < 16):
        hexData+= '0'
        hexData+=   hex(x)
    else:
        hexData+=   hex(x)
    
hexData=hexData.replace('0x','')

#hexData=''.join(hex(x) for x in data).replace('0x','').upper()


print("MHDR: ",MHDR,"\nDevAddr: ",SDevAddr,"\nFCTR: ",FCTR,"\nFCNT: ",FCNT,"\nFPORT: ",FPORT,"\nPayload: ",Payload,"\nMIC: ",MIC)
print(data)
print(hexData)






