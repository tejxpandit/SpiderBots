# Project : SpiderBots
# File : Command Executor
# Author : Tej Pandit
# Date : Jan 2024

from agent import Agency, Agent
from actions import Actions

class Executor():

    def __init__(self):
        self.agency = None

    def setAgency(self, agency):
        self.agency = agency

    def parseCommands(self, commands):
        name = commands[0]
        act = commands[1]
        tar = commands[2]
        des = commands[3]
    
        if name != None:
            ag = self.agency.agents[name]
            
            if act == None:
                 # IDLE
                print("Idle")
            if act == "move":
                if tar != None:
                    # MOVE
                    ag.move()
            elif act == "stop":
                # STOP
                ag.stop()
            elif act == "look":
                if tar != None:
                    # LOOK
                    ag.look()
            elif act == "chase":
                if tar != None:
                    # CHASE
                    ag.chase()
            elif act == "dance":
                # DANCE
                ag.dance()
            else:
                # IDLE
                print("Idle")
