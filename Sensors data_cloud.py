
# This code is for receiving data from arduino to Raspberry Pi
import serial
import time
import paho.mqtt.client as mq
c=mq.Client()
s=serial.Serial('/dev/ttyACM0',9600)

while True:
    data=s.readline()
    data=data.decode()
    data=data.split(',')
    temp=data[0]
    proximity=data[1][:-2]
    print("temp is",temp)
    print("proximity is ",proximity)
    c.connect('iot.eclipse.org',1883)
    time.sleep(1)
    
    c.publish('smartfactory001/temp',temp)
    time.sleep(1)
    c.publish('smartfactory001/proximity',proximity)
    c.disconnect()
    time.sleep(1)
