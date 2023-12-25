# Project : SpiderBots
# File : Actions Class for all effector robot actions
# Author : Tej Pandit
# Date : Dec 2023

from agent import Agent

class Actions():

    def __init__(self, agent=None, target=None, descriptor=None):
        self.agent = agent
        self.target = target
        self.descriptor = descriptor

    def Move(self):
        print("Moving")
    
    def Stop(self):
        print("Stop")

    def Look(self):
        print("Looking")

    def Chase(self):
        print("Chasing")

    def Dance(self):
        print("Dancing")