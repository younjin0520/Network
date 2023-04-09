#!/usr/bin/env python
# coding: utf-8

from socket import *
serverPort =12000

#Create server's socket
#Using IPv4, TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

#binding
serverSocket.bind(('',serverPort))
#Maximum number of queued connections  = 1
serverSocket.listen(1)
print("The server is ready to receive: ")

#loop to wait for a client connection and its message
try:
    while True:
        connectionSocket, clientAddress = serverSocket.accept()
        #buffer size=2048
        message = connectionSocket.recv(2048)
        #byte to string
        modifiedMessage = message.decode().upper()
        #string to byte
        #Send the modified messages
        connectionSocket.send(modifiedMessage.encode()) 
        connectionSocket.close()
except KeyboardInterrupt:
    print("Press Ctrl-C to terminate while statement")
    pass

