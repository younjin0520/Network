#!/usr/bin/env python
# coding: utf-8

# In[1]:


from socket import *
serverName = "127.0.0.1"
serverPort = 12000


# In[4]:


#Create socket
clientSocket = socket(AF_INET, SOCK_STREAM)


# In[5]:


#Connect to server
clientSocket.connect((serverName, serverPort))


# In[6]:


message = input("Input message: ")


# In[7]:


clientSocket.send(message.encode())


# In[ ]:


modifiedMessage = clientSocket.recv(2048)


# In[ ]:


print(modifiedMessage.decode())
clientSocket.close()

