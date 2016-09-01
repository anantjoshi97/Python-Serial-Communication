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
		with open('test1','ab') as f:
			f.write(ser.readline())
			f.write('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
    		#print ser.readline()
    		#print('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
    	else:
        	continue
        	
#first try , successful
 
PIPE = subprocess.PIPE
process = subprocess.Popen(["predict", "-f" , "<satname>"],stdout=PIPE, stderr=PIPE, universal_newlines=0) 
stdout, stderr = process.communicate()

print stdout
if len(stderr)>0 :
	print "error" , stderr

#second try
"""
output = subprocess.check_output([])
"""
#third try
"""
output = subprocess.check_output([], universal_newlines = TRUE)
"""
