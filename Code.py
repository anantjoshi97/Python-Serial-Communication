import datetime 
import serial
import subprocess

def predict(s): 
	""" date/time in Unix format, the date and time in ASCII
       (UTC), the elevation of the satellite in degrees, the  azimuth  of  the
       satellite  in degrees, the orbital phase (modulo 256), the latitude (N)
       and longitude (W) of the satellite's  sub-satellite  point,  the  slant
       range  to  the  satellite  (in  kilometers),  the orbit number, and the
       spacecraft's sunlight visibility information.  For example:  1003611710
       Sat  20Oct01  21:01:50    11     6   164    51   72   1389  16669 * """
       
       ele = ''
       lat = ''
       lon = ''
       i = 0 #iterator
       qty_count = 0 #if this variable has value i, it means the ith quantity is being accessed

       while (qty_count < 10) :
       	if(s[i]==' '):
       		i = i + 1
       		continue
       	if(i>0 and s[i-1]==' '):
       		qty_count = qty_count + 1
       	if(qty_count == 5):
       		ele = ele + s[i]
       	if(qty_count == 8):
       		lat = lat + s[i]
       	if(qty_count == 9): #longitude
       		lon = lon + s[i]

       	return ele , lat , lon
       	.
 
ser = serial.Serial('/dev/ttyACM1' , 9600)


PIPE = subprocess.PIPE
while True:
	i = ser.inWaiting()
	if(i>0):
		with open('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()),'a+') as f:

			f.write('{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + ' ')

			if(ser.readline() == '*'):
				f.write(ser.readline() + " ") # star voltage written
			if(ser.readline() == "#"):
				f.write(ser.readline() + " ") # hash voltage written

			process = subprocess.Popen(["predict", "-f" , "<satname>"],stdout=PIPE, stderr=PIPE, universal_newlines=0) 
			stdout, stderr = process.communicate()
			ele , lat , lon = predict(stdout)
			f.write(ele + " ")
			f.write(lat + " ")
			f.write(lon + '\n')
    		
    	else:
        	continue
        	
