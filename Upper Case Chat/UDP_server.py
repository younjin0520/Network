#!/usr/bin/env python
# coding: utf-8

from socket import *
serverPort = 12000

#Create socket
#Using IPv4, UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM) 

serverSocket.bind(('', serverPort))
print("The server is ready to receive.")

try:
    while True:
        #size of buffer = 2048
        message, clientAddress = serverSocket.recvfrom(2048)
        modifiedMessage = message.decode().upper() 
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
except KeyboardInterrupt:
    print("Press Ctrl-C to terminate while statement")
    pass

