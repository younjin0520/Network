#!/usr/bin/env python
# coding: utf-8

from socket import*

#localhost
serverName = "127.0.0.1" 
serverPort = 12000

#Create socket and connect to server
#Using IPv4, TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

#Read user message
message = input("Input lowercase sentence: ")

#Send the message to server
clientSocket.send(message.encode())

#Receive modified message from server
#buffer size = 2048
modifiedMessage = clientSocket.recv(2048)

#Print and finish
print(modifiedMessage.decode())
clientSocket.close()

