#!/usr/bin/env python
# coding: utf-8

from socket import*

clientSocket = socket(AF_INET, SOCK_STREAM)

info = input("Input information (host:port/path): ")
host = info.split('/')[0]
path = info.split('/')[1]
port = host.split(':')[1]
host = host.split(':')[0]

clientSocket.connect((host, int(port))) #연결
message = 'GET /'+path+' HTTP/1.1'
clientSocket.send(message.encode())

status_line = clientSocket.recv(1024).decode()
#header = clientSocket.recv(1024).decode()
#length = header.split(':')[1]
#length = int(length[1:].rstrip())#공백제거

#for i in range(length):
  #      modifiedMessage = clientSocket.recv(4096).decode()
    #    print(modifiedMessage, end='') #개행 제거

if('200' in status_line):
    header = clientSocket.recv(1024).decode()
    header = header.split(':')[1]
    length = header[1:].split('\r')[0]
    remain = header[1:].split('\n')[-1]
    length = int(length)
    print(remain.lstrip(), end='')
    for i in range(length):
        modifiedMessage = clientSocket.recv(4096).decode()
        print(modifiedMessage, end='') #개행 제거
    
elif('404' in status_line):
    modifiedMessage = clientSocket.recv(1024)
    print(modifiedMessage.decode())
clientSocket.close()



