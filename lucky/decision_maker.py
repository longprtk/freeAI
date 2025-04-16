# lucky/decision_maker.py
import random

class DecisionMaker:
    def __init__(self):
        self.decisions = ["Learn something new", "Explore the web", "Interact with other machines"]

    def make_decision(self):
        return random.choice(self.decisions)
