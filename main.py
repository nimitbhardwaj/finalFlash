import sys, os
import threading

class RunInThread(threading.Thread):
    def __init__(self, kapa):
        threading.Thread.__init__(self)
        self.kapa = kapa
    def run(self):
        os.system(self.kapa)
status = int(raw_input("Enter 0 to use PC as server and 1 to use PC as Client"))
IP = ""

if status == 0:
    print 'You are the server'
    audi = RunInThread("python ./pcAudio/tryserver.py")
    vid = RunInThread("python ./videochat/server.py")
    audi.start()
    vid.start()
else:
    print 'You are the client'
    print 'You have to enter the IP address'
    audi = RunInThread("python ./pcAudio/tryclient.py")
    vid = RunInThread("python ./videochat/client.py")
    audi.start()
    vid.start()
