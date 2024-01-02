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

        
#-----------------------------------------------------------------
# GENERATOR 

# import pickle

# # Target File
# file = open("commands.pkl", 'wb')

# # File Generator
# pickle.dump(actions, file)
# pickle.dump(actions_key, file)
# pickle.dump(targets, file)
# pickle.dump(targets_key, file)
# pickle.dump(descriptors, file)
# pickle.dump(descriptors_key, file)
# pickle.dump(agent_metanames, file)
# pickle.dump(agent_names, file)

# # Close File
# file.close()

# # Test
# file = open('commands.pkl', 'rb')
# act = pickle.load(file)
# act_k = pickle.load(file)
# tar = pickle.load(file)
# tar_k = pickle.load(file)
# des = pickle.load(file)
# des_k = pickle.load(file)
# agm = pickle.load(file)
# agn = pickle.load(file)
# print(act)
# print(act_k)
# print(tar)
# print(tar_k)
# print(des)
# print(des_k)
# print(agm)
# print(agn)

# # Verify
# if len(act) == len(act_k):
#     print("Actions Balanced")
# else:
#     print ("Actions Imbalanced")

# if len(tar) == len(tar_k):
#     print("Targets Balanced")
# else:
#     print ("Targets Imbalanced")

# if len(des) == len(des_k):
#     print("Descriptors Balanced")
# else:
#     print ("Descriptors Imbalanced")

# if len(agm) == len(agn):
#     print("Agent Names Balanced")
# else:
#     print ("Agent Names Imbalanced")

# # Close File
# file.close()

# # Import File Function
# def importCommandList(self, commandFile="commands.pkl"):
#         file = open(commandFile, 'rb')
#         self.actions = pickle.load(file)
#         self.actions_key = pickle.load(file)
#         self.targets = pickle.load(file)
#         self.targets_key = pickle.load(file)
#         self.descriptors = pickle.load(file)
#         self.descriptors_key = pickle.load(file)
#         self.agent_metanames = pickle.load(file)
#         self.agent_names = pickle.load(file)
#         file.close()
