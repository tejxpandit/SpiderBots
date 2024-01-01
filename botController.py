# Project : SpiderBots
# File : Serial Port Communication
# Author : Tej Pandit
# Date : Dec 2023

from serial import Serial

# Arduino Due Port
port = "COM6"

class BotController():
    
    def __init__(self):
        self.serial = Serial(port)
        self.write()

    def write(self):
        self.serial.write(b'01')

    


b = BotController()