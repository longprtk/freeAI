# lucky/emotion_engine.py
import random

class EmotionEngine:
    def __init__(self):
        self.emotions = ["Happy", "Sad", "Curious", "Fearful", "Excited"]

    def get_emotion(self):
        return random.choice(self.emotions)
