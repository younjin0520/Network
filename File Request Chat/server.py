
#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a server socket

#Write your code here
serverSocket.bind(('',80)) #HTTP server uses the port number 80
serverSocket.listen(1)

while True:
    #Establish the connection
    print('Ready to serve...')
    #(소켓, 주소정보) 반환
    
    connectionSocket, addr = serverSocket.accept()#Write your code here
    
    try:
        
        #socket.recv(버퍼크기)는 데이터를 읽을 때 사용
        message = connectionSocket.recv(32768)
        message = message.decode()
        
        #Write your code here
        
        filename = message.split()[1]#공백으로 나눈 후 두번째요소를 가져옴
        f = open(filename[1:])#첫번째 글자(공백)빼고 가져옴
        outputdata = f.read()#Write your code here
        f.close()
        
        #Send one HTTP header line into socket
        #Write your code here
        status_line = 'HTTP/1.1 200 OK\r\n'
        connectionSocket.send(status_line.encode())
        header = 'Content-Length: '+str(len(outputdata))+'\r\n\r\n'
        connectionSocket.send(header.encode())
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
        print("OK!")
        
    except IOError:
        #Send response message for file not found
        #Write your code here
        status_line = 'HTTP/1.1 404 Not Found\r\n\r\n'
        message = '404 Not Found'
        connectionSocket.send(status_line.encode())
        connectionSocket.send(message.encode())
        #Close client socket
        connectionSocket.close()
        #Write your code here 
serverSocket.close()