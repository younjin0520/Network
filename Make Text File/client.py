#!/usr/bin/env python
# coding: utf-8

# In[5]:


#!/usr/bin/env python
# coding: utf-8

from socket import*

#localhost
serverName = "127.0.0.1" 
serverPort = 13000

#Create socket and connect to server
#Using IPv4, TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
print("Connection success. Waiting for response...")
print("==========Received data==========")
#Receive modified message from server
f=open('Received_data.txt','w')
modifiedMessage = clientSocket.recv(2048)
try:
    while modifiedMessage:
        f.write(modifiedMessage.decode())
        print(modifiedMessage.decode())
        modifiedMessage = clientSocket.recv(2048)
    print("=================================")
    print("Writing success!")
except Exception as e:
    print(e)   
#Print and finish
clientSocket.close()


# In[ ]:




