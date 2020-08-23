#Sending the data thorugh UART 
#UART PINOUT
#Rx -> GPIO15
#Tx -> GPIO14

# get the GPIO Library
import RPi.GPIO as GPIO
import serial
import time

#Open named port 
GPIO.cleanup()
ser = serial.Serial("/dev/ttyS0", 115200)


while True:
    ser.write(b"Hello from Raspberry Pi!\n")
    
ser.close() 