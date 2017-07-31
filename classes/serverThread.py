import socket
import threading

class ChessClient(threading.Thread):

    def __init__(self, ip, port):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.connect((ip, port))        
        self.client = socket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))
        self.start()

    def run(self): 
        while (True):   
            print("Connection de %s %s" % (self.ip, self.port))
            data = self.client.recv(2048)

    def sendData(self, data):
        self.client.send(data.encode())

class ChessServer(threading.Thread):

    def __init__(self, ip, port):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.bind((ip, port))
        print("Waiting for the client to connect")
        socket.listen()
        self.server, address = socket.accept()
        self.start()

    def run(self): 
        while (True):   
            print("Connection de %s %s" % (self.ip, self.port))
            data = self.server.recv(2048)

    def sendData(self, data):
        self.server.send(data.encode())
