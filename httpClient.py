# Project : SpiderBots
# File : Test : HTTP Client
# Author : Tej Pandit
# Date : Dec 2023

# import requests
# r = requests.get('http://192.168.0.106/26/off')
# print(r.text)

import socket
import time

# Create a client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
clientSocket.connect(("192.168.0.106", 80))

for i in range(5):

    # Send data to server
    action = "up\n"
    clientSocket.send(action.encode())

    time.sleep(0.1)

# # Receive data from server
# dataFromServer = clientSocket.recv(1024)

# # Print to the console
# print(dataFromServer.decode())

 