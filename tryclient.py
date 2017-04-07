#tryclient
import socket
import pyaudio
import time
import threading
import sys

# HOST=raw_input("Enter the ip of server")
HOST = sys.argv[1]
PORT=6001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

CHUNK=1024
FORMAT=pyaudio.paInt16
CHANNELS=1
RATE=44100

class sendRecord(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.WAVE_OUTPUT_FILENAME="sever_output.wav"
        self.frames=[]
        self.p=pyaudio.PyAudio()
        self.stream=self.p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
        self.sendData=''

    def run(self):
        self.sendRecordFun()
    def sendRecordFun(self):
        while 1:
            self.sendData=self.stream.read(CHUNK)
            s.sendall(self.sendData)
            print "client record send"
            #time.sleep(1)

class recievePlay(threading.Thread):
    def __init__(self):
	    threading.Thread.__init__(self)
	    self.WAVE_OUTPUT_FILENAME="client.wav"
	    self.frames=[]
	    self.p1=pyaudio.PyAudio()
	    self.stream1=self.p1.open(format=FORMAT,channels=CHANNELS,rate=RATE,output=True,frames_per_buffer=CHUNK)
	    self.data='123'

    def run(self):
        self.recievePlayfun()

    def recievePlayfun(self):
        self.data = s.recv(1024)
        self.stream1=self.p1.open(format=FORMAT,channels=CHANNELS,rate=RATE,output=True,frames_per_buffer=CHUNK)
        while self.data != '':
            self.stream1.write(self.data)
            self.data = s.recv(1024)
            print "client recieve play"
            #time.sleep(2)

threadone=sendRecord()
threadtwo=recievePlay()
threadone.start()
threadtwo.start()
