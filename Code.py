import datetime 
import serial
import subprocess

ser = serial.Serial('/dev/ttyACM1' , 9600)
#ser = serial.Serial('/dev/tty.usbserial', 9600) 
#ser = serial.Serial('/dev/ttyUSBx-1')
#ser = serial.Serial('/dev/ttySx-1')
#ser = serial.Serial('/dev/ttyCOMx') x = number after COM in Arduino IDE
while True:
	i = ser.inWaiting()
	if(i>0):	
    		print ser.readline()
    		print('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
    	else:
        	continue
#first try 
"""        	
process = subprocess.Popen([], stdout=PIPE, stderr=PIPE, universal_newlines=TRUE)
stdout, stderr = subprocess.process.communicate()
"""
#second try
"""
output = subprocess.check_output([])
"""
