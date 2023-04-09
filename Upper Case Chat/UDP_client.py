#!/usr/bin/env python
# coding: utf-8

from socket import *

#local host
serverName = "127.0.0.1"
serverPort = 12000

#Create socket
#Using IPv4, UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

#Read user message
message = input("Input lowercase sentence: ")

#send the message to server
clientSocket.sendto(message.encode(), (serverName, serverPort))

#Receive modified message from server
#size of buffer =2048
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

#byte to string
print(modifiedMessage.decode())
clientSocket.close()

