# Project : SpiderBots
# File : Command Parser
# Author : Tej Pandit
# Date : Jan 2024

import re
import string

class Commands():

    def __init__(self, storedData):
        self.text = ""
        self.words = ""
        self.parsedCommand = []

        self.actions = storedData["actions"]
        self.actions_key = storedData["actions_key"]
        self.targets = storedData["targets"]
        self.targets_key = storedData["targets_key"]
        self.descriptors = storedData["descriptors"]
        self.descriptors_key = storedData["descriptors_key"]
        self.agent_metanames = storedData["agent_metanames"]
        self.agent_names = storedData["agent_names"]

    def inputCommand(self, command):
        self.text = command

    def findKeyword_AgentName(self):
        for a_m in self.agent_metanames:
            for a_n in a_m:
                if a_n in self.words:
                    idx = self.agent_metanames.index(a_m)
                    nam = self.agent_names[idx]
                    #print(nam)
                    return nam
        return None

    def getKeyword_Action(self):
        for a_k in self.actions:
            for a in a_k:
                if a in self.words:
                    idx = self.actions.index(a_k)
                    act = self.actions_key[idx]
                    #print(act)
                    return act
        return None

    def getKeyword_Target(self):
        for t_k in self.targets:
            for t in t_k:
                if t in self.words:
                    idx = self.targets.index(t_k)
                    tar = self.targets_key[idx]
                    #print(tar)
                    return tar
        return None

    def getKeyword_Descriptor(self):
        for d_k in self.descriptors:
            for d in d_k:
                if d in self.words:
                    idx = self.descriptors.index(d_k)
                    des = self.descriptors_key[idx]
                    #print(des)
                    return des
        return None

    def parseCommand(self):
        self.words = re.sub('['+string.punctuation+']', '', self.text.lower()).split()
        print(self.words)

        nam = self.findKeyword_AgentName()
        act = self.getKeyword_Action()
        tar = self.getKeyword_Target()
        des = self.getKeyword_Descriptor()
        self.parsedCommand = [nam, act, tar, des]
        print(self.parsedCommand)
        return self.parsedCommand
