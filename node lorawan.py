print("LoRa Node  Code")


import serial
import time

#ser.close()

ser = serial.Serial("COM16",57600)
ser.timeout=10
ser.flushInput()


def factoryReset():
    
    ser.write(bytearray('sys factoryRESET\r\n','ascii'))
    msg=ser.readline()
    print("sys factoryRESET:  >>",msg) 
  
    
def getStatus(): 
    ser.flushInput()
    #get sf 
    ser.write(bytearray('radio get sf\r\n','ascii'))
    msg=ser.readline()
    print("Radio sf  >>",msg) 
  
    
    #code rating CR
    ser.write(bytearray('radio get cr\r\n','ascii'))
    msg=ser.readline()
    print("cr is >>",msg)    
    
    
    #get freq 
    ser.write(bytearray('radio get freq\r\n','ascii'))
    msg=ser.readline()
    print("Radio get freq >>",msg) 
    
      
    ser.write(bytearray('mac get rxdelay1\r\n','ascii'))
    msg=ser.readline()
    print("Delay rx1 >>",msg)    
      
    
    
    
def setRadioSetting():
    ser.flushInput()

    #mac pause
    ser.write(bytearray('mac pause\r\n','ascii'))
    msg=ser.readline()
    print("mac pause >>",msg)    
    
    #sf 12
    ser.write(bytearray('radio set sf sf7\r\n','ascii'))
    msg=ser.readline()
    print("Radio SF7 >>",msg)    
    ser.flushInput()
    
    
    #BW 125
    ser.write(bytearray('radio set bw 125\r\n','ascii'))
    msg=ser.readline()
    print("Radio BW125  >>",msg)    
    ser.flushInput()
    
    
    #set freq 
    ser.write(bytearray('radio set freq 902300000\r\n','ascii'))
    msg=ser.readline()
    print("Radio freq >>",msg) 
#mac resume
    ser.write(bytearray('mac resume\r\n','ascii'))
    msg=ser.readline()
    print("mac resume >>",msg)   
    ser.flushInput() 
    time.sleep(2)

def resetSys():
    #system reset
    ser.write(bytearray('sys reset\r\n','ascii'))
    msg=ser.readline()
    print("sys reset >>",msg)    


def setMACSetting():
#mac pause
    ser.write(bytearray('mac pause\r\n','ascii'))
    msg=ser.readline()
    print("mac pause >>",msg)    
    
    
    i=0
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
        ser.flushInput()
       
        
    ser.write(bytearray('mac set ch status 0 on\r\n','ascii'))
    msg=ser.readline()
    print("channel 0 status >> ",msg)    
    ser.flushInput()
    
      
    # set nwkSkey   
    ser.write(bytearray('mac set nwkskey 1029384756AFBECD5647382910DACFEB\r\n','ascii'))
    msg=ser.readline()
    print("network session key >> ",msg)    
    ser.flushInput()
    
      
    # set appSkey   
    ser.write(bytearray('mac set appskey AFBECD56473829100192837465FAEBDC\r\n','ascii'))
    msg=ser.readline()
    print("Application sessoin key >> ",msg)    
    ser.flushInput()
    
    
    #device address
    ser.write(bytearray('mac set devaddr 001B3109\r\n','ascii'))
    msg=ser.readline()
    print("Device Address >> ",msg)    
    ser.flushInput()
    
    
    ser.write(bytearray('mac set rxdelay1 5000\r\n','ascii'))
    msg=ser.readline()
    print("mac set rxw1 >>",msg)  
    ser.flushInput()
    
    
    ser.write(bytearray('mac save\r\n','ascii'))
    msg=ser.readline()
    print("mac save >>",msg)   
    ser.flushInput() 
    
    
    #mac resume
    ser.write(bytearray('mac resume\r\n','ascii'))
    msg=ser.readline()
    print("mac resume >>",msg)   
    ser.flushInput() 
    
    
setMACSetting() #resume the mac at the end

setRadioSetting() #pause the mac at the begining




#mac join
ser.write(bytearray('mac join abp\r\n','ascii'))
msg=ser.readline()
print("mac join >>",msg)    
ser.flushInput()




# trying downlink section
while 1:
    print("#################################")
    ser.flushInput()
    #mac send data
    ser.write(bytearray('mac tx uncnf 30 1234567\r\n','ascii'))
    msg=ser.readline()
    print("mac syntax >>",msg)   

    msg=ser.readline()
    print("mac final reply >>",msg)   
   
    print("*****************************")
    
    getStatus()

    time.sleep(3)



#ser.close()



ser.flushInput()
#mac send data
ser.write(bytearray('mac tx uncnf 30 5809\r\n','ascii'))
msg=ser.readline()
print("mac syntax >>",msg)   

msg=ser.readline()
print("mac final reply >>",msg)   
   