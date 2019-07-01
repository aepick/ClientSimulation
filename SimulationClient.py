#!/usr/bin/env python3
import socket
import time
import json
import sys
sensitiveData = {
    'user':'MyUsername',
    'password':'password1234'
}
connected = False
counter = 0
host = sys.argv[1]
port = int(sys.argv[2])                   # The same port as used by the server
while counter < 100:
    #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.connect((host, port))
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        connected = True
    except socket.error as error:
        counter += 1
        #print('error occurred trying again: '+ str(counter))
        connected = False
        s.close()
    if(connected == True):
        counter = 0
        try:
            data=(json.dumps(sensitiveData))
            #print(data)
            s.sendall(data.encode('utf-8'))
            data = s.recv(1024)
            print('Received', repr(data))
            connected = False
            time.sleep(2)
        except(KeyboardInterrupt):
            data = 'Exit'
            s.sendall(data.encode('utf-8'))
            s.close()
    
    time.sleep(2)
    
