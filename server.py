import socket, videosocket
from videofeed import VideoFeed
def getMyIP():
    mySock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    mySock.connect(('8.8.8.8', 80))
    ip = mySock.getsockname()[0]
    mySock.close()
    return ip

class Server:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip = getMyIP()
        print 'Your IP is ' + ip
        self.server_socket.bind((ip, 6000))
        self.server_socket.listen(5)
        self.videofeed = VideoFeed(1,"server",1)
        print "TCPServer Waiting for client on port 6000"

    def start(self):
        while 1:
            client_socket, address = self.server_socket.accept()
            print "I got a connection from ", address
            vsock = videosocket.videosocket(client_socket)
            while True:
                frame=vsock.vreceive()
                self.videofeed.set_frame(frame)
                frame=self.videofeed.get_frame()
                vsock.vsend(frame)

if __name__ == "__main__":
    server = Server()
    server.start()
