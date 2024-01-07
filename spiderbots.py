# Project : SpiderBots
# File : SpiderBots Project Launcher
# Author : Tej Pandit
# Date : Jan 2024

from dataGenerator import DataStorage
from audioController import AudioRecordController
from transcribeAudio import TranscribeAudio
from commands import Commands
from executor import Executor
from agent import Agency, Agent
from objectDetector import ObjectDetector

dataStore = DataStorage()
audioController = AudioRecordController()
audioTranscriber = TranscribeAudio()
objDetector = ObjectDetector()

commander = Commands(dataStore.data)
agency = Agency(dataStore.data, objDetector)
agency.createAgents()
executor = Executor()
executor.setAgency(agency)

print("READY!")
endProgram = False
while not endProgram:

    print("Hold *Space* to Issue Commands")
    endProgram = audioController.startKeyboardListener()
    
    if not endProgram:
        raw_text = audioTranscriber.transcribe()
        commander.inputCommand(raw_text)
        commands = commander.parseCommand()
        executor.parseCommands(commands)

objDetector.terminate()