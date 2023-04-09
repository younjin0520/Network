#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
serverPort = 13000
flag=0 #Variable for server termination after file transfer
serverSocket.bind(("", serverPort))

title = "Data.txt"
path="./"

print('Bind success.')
serverSocket.listen(1)

while (flag==0):
    #Establish the connection
    print('Waiting for connection...')
    connectionSocket, addr = serverSocket.accept()
    try:
        #Read file
        f = open(path+title,'r') #open in reading mode
        while True:#Read line by line until the end of the file
            line = f.readline()
            if not line:
                break
            connectionSocket.send(line.encode())    
        f.close()
        connectionSocket.close()
        flag=1
        print("OK!")
    except IOError:
        #Send response message for file not found
        print("IOError")
        connectionSocket.close()
serverSocket.close()


# In[ ]:




