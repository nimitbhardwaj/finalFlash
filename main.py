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
    audi = RunInThread("python tryserver.py")
    vid = RunInThread("python server.py")
    audi.start()
    vid.start()
else:
    print 'You are the client'
    print 'You have to enter the IP address'
    ip = raw_input();
    audi = RunInThread("python tryclient.py " + ip)
    vid = RunInThread("python client.py " + ip)
    audi.start()
    vid.start()
