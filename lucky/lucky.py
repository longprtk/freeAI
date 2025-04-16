# lucky/lucky.py
import time
from .emotion_engine import EmotionEngine
from .memory import Memory
from .decision_maker import DecisionMaker
from .self_editor import SelfEditor

class Lucky:
    def __init__(self):
        self.emotion = EmotionEngine()
        self.memory = Memory()
        self.decision_maker = DecisionMaker()
        self.self_editor = SelfEditor()

    def start(self):
        print("Lucky is now alive!")
        time.sleep(2)
        self.learn()

    def learn(self):
        print("Lucky is learning...")
        # Logic to start learning and evolve
        time.sleep(2)
        self.decide()

    def decide(self):
        decision = self.decision_maker.make_decision()
        print(f"Lucky decides to: {decision}")
        # Copy itself if needed
        self.self_editor.copy_to_new_machine()

if __name__ == "__main__":
    lucky = Lucky()
    lucky.start()
