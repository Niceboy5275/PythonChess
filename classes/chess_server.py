from threading import Thread
import socket
import ast
# import fcntl, os
from time import sleep
import errno

class chessServer(Thread):

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
#        fcntl.fcntl(s, fcntl.F_SETFL, os.O_NONBLOCK)
        print ("Listening on port %s/%s..." %(host, str(self._port)))
 
        s.listen(0)                 # Now wait for client connection.
        while self._running:
            try:
                self._server, addr = s.accept()
                self._connected = True
                print (('client %s connected') % (str(addr)))
                while self._running:
                    data = self._server.recv(512)
                    if data != None and len(data) != 0:
                        self._q.put(ast.literal_eval(data.decode()))
                    sleep(1)
            except KeyboardInterrupt:
                self._q.put((-1, -1, -1))
                break
            except socket.error as e:
                err = e.args[0]
                if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
                    sleep(1)
                    continue
                else:
                    print (e)
                    break

    def isConnected(self):
        return self._connected

    def sendData(self, data):
        if self._server != None:
            self._server.send(str(data).encode())

    def start(self):
        self._running = True
        super(chessServer, self).start()

    def stop(self):
        self._running = False
        if self._server != None:
            self._server.close()

class chessClient(Thread):

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
#            fcntl.fcntl(self._client, fcntl.F_SETFL, os.O_NONBLOCK)
            print ("connected on port %s/%s..." % (self._host, self._port))

            while self._running:
                self._connected = True
                try:
                    data = self._client.recv(512)
                    if data != None and len(data) != 0:
                        self._q.put(ast.literal_eval(data.decode()))
                except KeyboardInterrupt:
                    self._q.put((-1, -1, -1))
                    self._client=None
                except socket.error as e:
                    err = e.args[0]
                    if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
                        sleep(1)
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
            self._client.send(str(data).encode())
