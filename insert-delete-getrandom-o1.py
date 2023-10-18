import random

class RandomizedSet:

    def __init__(self):
        self.init = set()

    def insert(self, val: int) -> bool:
        if val in self.init:
            return False
        self.init.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.init:
            return False
        self.init.remove(val)
        return True

    def getRandom(self) -> int:
        if self.init:
            return random.choice(list(self.init))
        return None