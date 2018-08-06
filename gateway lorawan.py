print("LORA Simulation Code")


import serial
import time



ser = serial.Serial("COM8",57600)
ser.timeout=None
ser.flush()


#mac pause
ser.write(bytearray('sys reset\r\n','ascii'))
msg=ser.readline()
print("sys reset >>",msg)    




#mac pause
ser.write(bytearray('mac pause\r\n','ascii'))
msg=ser.readline()
print("mac pause >>",msg)    



i=1

#disable all channels
while True:
    
    
    frame='mac set ch status ';
    frame =frame + str(i)+' off'
    

    ser.write(bytearray(frame,'ascii'))
    ser.write(bytearray('\r\n','ascii'))


    msg=ser.readline()
    print(frame,"   ", i,"   ",msg)    
   
    if (i == 71):
        break
    i=i+1
    ser.flush()
  
  
    
ser.write(bytearray('mac set ch status 0 on\r\n','ascii'))
msg=ser.readline()
print("channel 0 status >> ",msg)    


ser.write(bytearray('mac save\r\n','ascii'))


#sf 12
ser.write(bytearray('radio set sf sf7\r\n','ascii'))
msg=ser.readline()
print("Radio SF7 >>",msg)    


#BW 125
ser.write(bytearray('radio set bw 125\r\n','ascii'))
msg=ser.readline()
print("Radio BW125  >>",msg)    


#set freq 
ser.write(bytearray('radio set freq 902300000\r\n','ascii'))
msg=ser.readline()
print("Radio freq >>",msg) 

   


#get freq 
ser.write(bytearray('radio get freq\r\n','ascii'))
msg=ser.readline()
print("Radio get freq >>",msg) 

   


#get sf 
ser.write(bytearray('radio get sf\r\n','ascii'))
msg=ser.readline()
print("Radio sf  >>",msg) 



#code rating CR
ser.write(bytearray('radio get cr\r\n','ascii'))
msg=ser.readline()
print("cr is >>",msg)    







while (1):    
    ser.flush()
    
#sf 12
    ser.write(bytearray('radio set sf sf7\r\n','ascii'))
    msg=ser.readline()
    print("Radio SF7 >>",msg)    

    #Radio Test
    ser.write(bytearray('radio rx 0\r\n','ascii'))
    msg=ser.readline()
    print("radio rx 0   >>",msg)    
    
    
    msg=ser.readline()
    print("payload is = ",msg)    

  
ser.close()
