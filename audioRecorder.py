# Project : SpiderBots
# File : Audio Recorder
# Author : Tej Pandit
# Date : Jan 2024

import pyaudio
import wave
import threading

class AudioRecorder():

    def __init__(self, chunk=8192, format=pyaudio.paInt16, channels=2, rate=44100, seconds=5, file_name="output.wav"):
        self.chunk = chunk
        self.format = format
        self.channels = channels
        self.rate = rate
        self.filename = file_name

        self.frames = []
        self.rec = pyaudio.PyAudio()
        self.stream = self.rec.open(format=self.format,
                                channels=self.channels,
                                rate=self.rate,
                                input=True,
                                frames_per_buffer=self.chunk)
        

    def record(self, e_startRecording, e_stopRecording):
        if(e_startRecording.wait()):
            while(not e_stopRecording.isSet()):
                #print("inside recorder")
                try:
                    data = self.stream.read(self.chunk)
                    self.frames.append(data)
                except IOError: 
                    print('warning: dropped frame')
                    #pass
            self.saveRecording()
            self.resetRecordedFrameBuffer()
            e_startRecording.clear()
            e_stopRecording.clear()

    def resetRecordedFrameBuffer(self):
        self.frames = []

    def saveRecording(self):
        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.rec.get_sample_size(self.format))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(self.frames))
        wf.close()

    def endRecorder(self):
        self.stream.stop_stream()
        self.stream.close()
        self.rec.terminate()
