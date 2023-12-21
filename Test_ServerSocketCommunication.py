# Project : SpiderBots
# File : Test : Server Socket Communication (Python)
# Author : Tej Pandit
# Date : Dec 2023

import socket

s = socket.socket()         
s.bind(('0.0.0.0', 8090 ))
s.listen(0)                 

while True:

    # Handle Wireless Client : SpiderBot
    client, addr = s.accept()
    msg = client.recv(100).decode()
    words = msg.split()

    if(len(words)>0):
        name = words[0]
        dist_buffer = words[1:9]
        print(name)
        print(dist_buffer)

    client.close()