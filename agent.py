# Project : SpiderBots
# File : Agent Class for managing robot states, actions, sensors, data
# Author : Tej Pandit
# Date : Dec 2023

import cv2
import requests
import pandas

states = ["inactive", "active"]

class Agent:
    def __init__(self, objDetector):
        self.objDetector = objDetector
        self.state = None
        self.name = None
        self.metaname = None
        self.action = None
        self.target = None
        self.description = None
        self.ip = None
        self.cam = None
        self.detectedObjects = None
    
    #def startLIDAR(self):

    def move(self):
        print("Moving")
        
    def stop(self):
        print("Stopping")

    def look(self):
        print("Looking")

    def chase(self):
        print("Chasing")

    def dance(self):
        print("Dancing")

    def startCamera(self):
        self.cam = cv2.VideoCapture("http://" + self.ip + ":81/stream")
        self.set_resolution("http://" + self.ip, index=8)

    def viewCamera(self):
        if self.cam.isOpened():
            ret, frame = self.cam.read()

            if ret:
                img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                cv2.imshow(self.name, img)

    def detectObjects(self):
        if self.cam.isOpened():
            ret, frame = self.cam.read()

            if ret:
                self.detectedObjects = []
                img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                objects = self.objDetector.detect(self.name, img, True)
                results = objects.pandas().xyxy[0]
                # for obj in range(len(results.index)):
                #     print(results.loc[obj])
                for obj in range(len(results.index)):
                    if results.loc[obj].at["confidence"] > 0.5:
                        self.detectedObjects.append(results.loc[obj].at["name"])

                return self.detectedObjects

    def set_resolution(url: str, index: int=1, verbose: bool=False):
        try:
            if verbose:
                resolutions = "10: UXGA(1600x1200)\n9: SXGA(1280x1024)\n8: XGA(1024x768)\n7: SVGA(800x600)\n6: VGA(640x480)\n5: CIF(400x296)\n4: QVGA(320x240)\n3: HQVGA(240x176)\n0: QQVGA(160x120)"
                #print("available resolutions\n{}".format(resolutions))

            if index in [10, 9, 8, 7, 6, 5, 4, 3, 0]:
                requests.get(url + "/control?var=framesize&val={}".format(index))
            else:
                print("Wrong index")
        except:
            print("SET_RESOLUTION: something went wrong")

class Agency:
    def __init__(self, storedData, objDetector):
        # self.actions = storedData["actions"]
        # self.actions_key = storedData["actions_key"]
        # self.targets = storedData["targets"]
        # self.targets_key = storedData["targets_key"]
        # self.descriptors = storedData["descriptors"]
        # self.descriptors_key = storedData["descriptors_key"]
        self.objDetector = objDetector
        self.agent_metanames = storedData["agent_metanames"]
        self.agent_names = storedData["agent_names"]
        self.agent_IPs = storedData["agent_IPs"]
        self.agents = {}

    def createAgents(self):
        for idx, name in enumerate(self.agent_names):
            ag = Agent(self.objDetector)
            ag.state = "inactive"
            ag.name = name
            ag.metaname = self.agent_metanames[idx]
            ag.ip = self.agent_IPs[idx]

            self.agents[ag.name] = ag
            
            #ag.startLIDAR()
            ag.startCamera()

    def Terminate(self):
        for ag in self.agents:
            ag.cam.release()

    # def Activate(self):
    #     self.state = "active"

    # def Deactivate(self):
    #     self.state = "inactive"

    # def setAction(self, action):
    #     self.action = action

    # def setTarget(self, action):
    #     self.action = action

    # def setDescription(self, action):
    #     self.action = action   
