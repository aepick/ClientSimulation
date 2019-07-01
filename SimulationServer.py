#!/usr/bin/env python3
import socket
import sys
import json
host = sys.argv[1]        # Symbolic name meaning all available interfaces
port = int(sys.argv[2])    # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

print(host , port)
while True:
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)
    try:
        data = conn.recv(1024)
        if not data:
            print('Not Data' + data.decode())
            #print(data) 
            break
        print ("Client Says: "+data.decode())
        conn.sendall(b"FLAG")
        if(data.decode() == 'Exit'):
            break
    except socket.error:
        print ("Error Occured.")
        break
conn.close()
