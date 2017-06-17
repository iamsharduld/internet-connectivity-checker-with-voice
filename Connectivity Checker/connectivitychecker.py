import urllib2
import time,datetime
import pyaudio #to be installed
import wave
import sys




def convertTime(t):				#Converts time in seconds to hours,minutes,seconds
	hours = t/3600
	val = t%3600
	minutes = val/60
	val = val%60
	seconds = val
	return (str(int(hours))+"h"+str(int(minutes))+"m"+str(int(seconds))+"s")





def isConnected():
    try:
        response=urllib2.urlopen('http://216.58.192.142', timeout=1)
        return 1
    except urllib2.URLError as err: pass
    except : 
    	return 2
    return 0




def play(s):

	CHUNK = 1024
	if(s=="Connected"):
		wf = wave.open('Connected.wav', 'rb')
	else:
		wf = wave.open('Disconnected.wav','rb')
	p = pyaudio.PyAudio()

	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
	                channels=wf.getnchannels(),
	                rate=wf.getframerate(),
	                output=True)

	data = wf.readframes(CHUNK)

	while data != '':
	    stream.write(data)
	    data = wf.readframes(CHUNK)

	stream.stop_stream()
	stream.close()
	p.terminate()



if(isConnected()==0):
	print "Disconnected on",
	now = datetime.datetime.now()
	print now		
	interval = 1
	play("Disconnected")
	flag = 0
else:
	print "Connected on",
	now = datetime.datetime.now()
	print now		
	interval = 1
	play("Connected")
	flag = 1


totalDisconnectedTime = 0
connect = time.time()
disconnect = time.time()
returnValue1 = 0
returnValue2 = 0
interval = 1
while(True):
	if(returnValue1==0 and returnValue2==1 and flag==0):
		connect = time.time()
		totalDisconnectedTime+=connect-disconnect
		print "for",convertTime(connect-disconnect)
		print "Total Disconnected time ",convertTime(totalDisconnectedTime)
		print "Connected on",
		now = datetime.datetime.now()
		print now
		interval = 5
		play("Connected")
		flag = 1
	elif(returnValue1==1 and returnValue2==0 and flag==1):
		disconnect = time.time()
		print "for",convertTime(disconnect-connect)
		print "Disconnected on",
		now = datetime.datetime.now()
		print now		
		interval = 1
		play("Disconnected")
		flag = 0
	elif(returnValue1==1 and returnValue2==1 and flag==0):
		connect = time.time()
		totalDisconnectedTime+=connect-disconnect	
		print "for",convertTime(connect-disconnect)
		print "Total Disconnected time ",convertTime(totalDisconnectedTime)
		print "Connected on",
		now = datetime.datetime.now()
		print now		
		interval = 5
		play("Connected")
		flag = 1
	elif(returnValue1==0 and returnValue2==0 and flag==1):
		disconnect = time.time()	

		print "for",convertTime(disconnect-connect)
		print "Disconnected on",
		now = datetime.datetime.now()
		print now		
		interval = 5
		play("Disconnected")
		interval = 1
		flag = 0
	returnValue1 = isConnected()
	time.sleep(interval)
	returnValue2 = isConnected()
	#print returnValue1,returnValue2





