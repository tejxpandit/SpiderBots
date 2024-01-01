# Project : SpiderBots
# File : Audio Record Controller
# Author : Tej Pandit
# Date : Dec 2023

import threading
from pynput import keyboard

from audioRecorder import AudioRecorder

class AudioRecordController():

    def __init__ (self, recordKey=keyboard.Key.space, exitKey=keyboard.Key.esc):
        self.recorder = AudioRecorder()
        self.e_startRecording = threading.Event()
        self.e_stopRecording = threading.Event()
        self.recordKey = recordKey
        self.exitKey = exitKey
        self.recorder_thread = threading.Thread(name='audio-recorder', target=self.recorder.record, args=(self.e_startRecording, self.e_stopRecording))
        self.listener = None
        self.endProgram = None

    def on_press(self, key):
        if key == self.recordKey:
            if not self.e_startRecording.isSet():
                print('- Started Recording -')
                self.e_stopRecording.clear()
                self.e_startRecording.set()
                #self.recorder_thread = None
                self.recorder_thread = threading.Thread(name='audio-recorder', target=self.recorder.record, args=(self.e_startRecording, self.e_stopRecording))
                self.recorder_thread.start()
        elif key == self.exitKey:
            print('- Exiting Recorder -')
            self.endProgram = True
            self.recorder.endRecorder()
            self.listener.stop()
        else:
            print('incorrect character {0}, press cmd_l'.format(key))

    def on_release(self, key):
        if key == self.recordKey:
            print('- Stopped Recording -')
            self.e_stopRecording.set()
            self.e_startRecording.clear()
            self.recorder_thread.join()
            self.listener.stop()

            # --> for SINGLE RECORD LOOP only
            # self.recorder.endRecorder()

    def startKeyboardListener(self):
            self.endProgram = False
            with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as self.listener:
                self.listener.join()
            return self.endProgram

        # self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        #     self.listener.start()
        # listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        # listener.start()
