import speech_recognition as sr
import numpy as np
from transformers import pipeline
import threading
import queue

class SpeechAnalyzer:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.sentiment_pipeline = pipeline("sentiment-analysis")
        self.audio_queue = queue.Queue()
        
    def calibrate_microphone(self):
        """Calibrate for ambient noise"""
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
    
    def listen_live(self, callback):
        """Real-time speech recognition"""
        self.calibrate_microphone()
        print("🔴 Listening... Speak now!")
        
        with self.microphone as source:
            while True:
                try:
                    audio = self.recognizer.listen(source, timeout=1, phrase_time_limit=5)
                    text = self.recognizer.recognize_google(audio)
                    
                    # Analyze sentiment
                    sentiment = self.sentiment_pipeline(text)[0]
                    
                    result = {
                        "text": text,
                        "sentiment": sentiment['label'],
                        "confidence": sentiment['score']
                    }
                    
                    callback(result)
                    self.audio_queue.put(result)
                    
                except sr.WaitTimeoutError:
                    pass
                except sr.UnknownValueError:
                    pass
                except sr.RequestError:
                    print("Speech service error")
