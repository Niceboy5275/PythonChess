from threading import Thread
import socket
import ast
from time import sleep
import errno

class chessServer(Thread): #pragma: no cover

    def __init__(self, q, port):
        Thread.__init__(self)
        self._q = q
        self._server = None
        self._port = port
        self._running = False
        self._connected = False

    def run(self):
        s = socket.socket()         # Create a socket object
        host = socket.gethostname() # Get local machine name
        s.bind((host, self._port))        # Bind to the port
        s.settimeout(60.0)
        print ("Listening on port {h}/{p}...".format(p=self._port, h=host))
 
        s.listen(0)                 # Now wait for client connection.
        while self._running:
            try:
                self._server, addr = s.accept()
                self._connected = True
                print (('client %s connected') % (str(addr)))
                while self._running:
                    data = self._server.recv(512)
                    if data != None and len(data) != 0:
                        print ("SERVER : Data received" + str(data.decode()))
                        self._q.put(ast.literal_eval(data.decode()))
                    sleep(1)
            except KeyboardInterrupt:
                self._q.put((-1, -1, -1))
                break
            except socket.error as e:
                err = e.args[0]
                if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
                    continue
                else:
                    print (e)
                    break

    def isConnected(self):
        return self._connected

    def sendData(self, data):
        if self._server != None:
            print ("SERVER : Data sent" + str(data))
            self._server.send(str(data).encode())

    def start(self):
        self._running = True
        super(chessServer, self).start()

    def stop(self):
        self._running = False
        if self._server != None:
            self._server.close()

class chessClient(Thread): #pragma: no cover

    def __init__(self, q, host, port):
        Thread.__init__(self)
        self._q = q
        self._client = None
        self._host = host
        self._port = port
        self._running = False
        self._connected = False

    def isConnected(self):
        return self._connected

    def start(self):
        self._running = True
        super(chessClient, self).start()

    def stop(self):
        self._running = False
        self._client.close()

    def run(self):
        try:
            self._client = socket.socket()         # Create a socket object
            self._client.connect((self._host, self._port))        # Connect to the port
            self._client.settimeout(60.0)
            print ("connected on port {h}/{p}...".format(h=self._host, p=self._port))

            while self._running:
                self._connected = True
                try:
                    data = self._client.recv(512)
                    if data != None and len(data) != 0:
                        print ("CLIENT data received : " + str(data.decode()))
                        self._q.put(ast.literal_eval(data.decode()))
                except KeyboardInterrupt:
                    self._q.put((-1, -1, -1))
                    self._client=None
                except socket.error as e:
                    err = e.args[0]
                    if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
                        continue
                    else:
                        # a "real" error occurred
                        print (e)
        except KeyboardInterrupt:
            self._client=None
        except socket.error as e:
            self._client=None
            print (e)

    def sendData(self, data):
        if self._client != None:
            print ("CLIENT data sent : " + str(data))
            self._client.send(str(data).encode())
