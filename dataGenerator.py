# Project : SpiderBots
# File : Knowledge Base Generator
# Author : Tej Pandit
# Date : Jan 2024

from agent import Agent

class DataStorage:

    #-----------------------------------------------------------------
    # COMMANDS 

    actions = [["move", "go", "come", "walk", "run", "crawl"], 
                ["stop", "break", "relax", "sleep"],
                ["look", "find", "search", "where"], 
                ["chase", "catch"], 
                ["dance"]]

    actions_key = ["move",
                "stop",
                "look", 
                "chase", 
                "dance"]

    targets = [["human", "you", "me", "person", "him", "her"],
                ["apple"],
                ["orange"],
                ["car"],
                ["cup"],
                ["bottle"],
                ["plant"]]

    targets_key = ["human",
                "apple",
                "orange",
                "car",
                "cup",
                "bottle",
                "plant"]

    #YOLO 
    '''
    targets_key = ["person",
                "apple",
                "orange",
                "car",
                "cup",
                "bottle",
                "potted plant"]
    '''


    descriptors = [["red", "green", "blue", "yellow", "white", "black"],
                ["small", "big"]]

    descriptors_key = [["colors"], 
                ["size"]]

    #-----------------------------------------------------------------
    # AGENTS

    agent_metanames = [["crawly", "crawley", "crowley", "krolley"],
                ["buggy", "bugy", "buggee", "bagi", "bucky", "baggy", "buggie"]]

    agent_names = ["CRAWL-E",
                "BUG-E"]

    agent_IPs = ["192.168.0.104", 
                "192.168.0.107"]

    #-----------------------------------------------------------------
    # FUNCTIONS

    def __init__(self):
        self.data = {}
        self.loadAllData()

    def loadAllData(self):
        self.data["actions"] = self.actions
        self.data["actions_key"] = self.actions_key
        self.data["targets"] = self.targets
        self.data["targets_key"] = self.targets_key
        self.data["descriptors"] = self.descriptors
        self.data["descriptors_key"] = self.descriptors_key
        self.data["agent_metanames"] = self.agent_metanames
        self.data["agent_names"] = self.agent_names
        self.data["agent_IPs"] = self.agent_IPs
        #print(self.data)

    def getData(self):
        return self.data

        
