import datetime 
import serial
import subprocess



def predict(s) :	
	""" date/time in Unix format, the date and time in ASCII
       (UTC), the elevation of the satellite in degrees, the  azimuth  of  the
       satellite  in degrees, the orbital phase (modulo 256), the latitude (N)
       and longitude (W) of the satellite's  sub-satellite  point,  the  slant
       range  to  the  satellite  (in  kilometers),  the orbit number, and the
       spacecraft's sunlight visibility information.  For example:  1003611710
       Sat  20Oct01  21:01:50    11     6   164    51   72   1389  16669 * """
	
	ele = '' #will give slant range
	lat = ''
	lon = ''
	i = 0 #iterator
	qty_count = 1 #if this variable has value i, it means the ith quantity is being accessed

	while (qty_count < 10) :
		if(s[i]==' '):
			i = i + 1
			continue
		if(i>0 and s[i-1]==' ' and s[i]!=' '):
			qty_count = qty_count + 1
			
		if(qty_count == 10):
			ele = ele + s[i]
		if(qty_count == 8):
			lat = lat + s[i]
		if(qty_count == 9): #longitude
			lon = lon + s[i]
		i = i + 1

	return ele , lat , lon

       
 
ser = serial.Serial('/dev/ttyACM0' , 9600)


PIPE = subprocess.PIPE

file_name = 'Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
with open(file_name,'a+') as f:
	f.write("Beginning \n")

while True:
	i = ser.inWaiting()
	#print "i =" , i
	if(i>0):
		with open(file_name,'a+') as f:

			f.write('{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + ' ')

			#f.write(ser.readline() + " ") # star voltage written
			data = ""
			string = ser.readline()
			length = len(string)
			for k in range(length-2):
				data = data +  string[k]
			f.write(data + " ")
			
			process = subprocess.Popen(["predict", "-f" , "FUN"],stdout=PIPE, stderr=PIPE, universal_newlines=0) 
			stdout, stderr = process.communicate()
			ele , lat , lon = predict(stdout)
			f.write(ele + " " + lat + " " + lon + '\n')
			#f.write(lat + " ")
			#f.write(lon + '\n') 
    		
    	else:
        	continue
        	
