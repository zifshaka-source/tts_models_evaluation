
import whisper
import sounddevice as sd
import numpy as np
from textblob import TextBlob

class VoiceEngine:
    def __init__(self):
        self.model = whisper.load_model("base")
        self.sample_rate = 16000
        self.is_listening = True

    def listen(self):
        """Records audio and transcribes it."""
        # In production, this would use a VAD (Voice Activity Detection) trigger
        duration = 5 # 5 second window
        recording = sd.rec(int(duration * self.sample_rate), samplerate=self.sample_rate, channels=1)
        sd.wait()
        
        # Transcribe
        result = self.model.transcribe(recording.flatten())
        text = result["text"]
        
        # Sentiment Analysis
        sentiment = TextBlob(text).sentiment.polarity # -1.0 to 1.0
        emotion = "Neutral"
        if sentiment > 0.3: emotion = "Positive"
        elif sentiment < -0.3: emotion = "Negative/Stressed"
        
        return text, emotion

    def start_listening_loop(self, callback):
        while self.is_listening:
            text, emotion = self.listen()
            if text.strip():
                callback(text, emotion)
