# Audio Transcription
# Author : Tej Pandit
# Date : Jan 2023

import whisper
import torch

class TranscribeAudio():

    # Force CPU (faster for small commands)
    torch.cuda.is_available = lambda : False
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    def __init__(self, model="base", filename="output.wav"):
        self.model = whisper.load_model(model)
        self.filename = filename

    def setFilename(self, filename):
        self.filename = filename

    def transcribe(self):
        result = self.model.transcribe(self.filename)
        return(result["text"])

    