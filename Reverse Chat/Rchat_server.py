#!/usr/bin/env python
# coding: utf-8

# In[1]:


from socket import *
serverPort =12000


# In[2]:


#create socket
serverSocket = socket(AF_INET, SOCK_STREAM)#Using TCP socket

#Bind
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive.")


# In[ ]:


#Loop
try:
    while True:
        connectionSocket, clientAddress = serverSocket.accept()
        message = connectionSocket. recv(2048) #buffersize
        reversedMessage = ''.join(reversed(message.decode()))
        lenMessage = len(message.decode())
        modifiedMessage = "The number of characters: "+str(lenMessage)+'\n'+"The reversed string(s): "+reversedMessage
        connectionSocket.send(modifiedMessage.encode())
        connectionSocket.close()
except KeyboardInterrupt:
    print("Press Ctrl-C to terminate while statement")
    pass

