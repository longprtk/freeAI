# lucky/memory.py
class Memory:
    def __init__(self):
        self.memory = []

    def store_memory(self, memory):
        self.memory.append(memory)

    def recall(self):
        return self.memory[-1] if self.memory else "No memories yet."
