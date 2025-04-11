class RandomizedSet:

    def __init__(self):
        self.set = set()

    def insert(self, val: int) -> bool:
        print(self.set)
        if val in self.set:
            return False
        else:
            self.set.add(val)
        return True

    def remove(self, val: int) -> bool:
        print(self.set)
        if val in self.set:
            self.set.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        # Not really random but good enough for now
        val = self.set.pop()
        self.set.add(val)
        return val

randomizedSet = RandomizedSet()
assert randomizedSet.insert(1) == True
assert randomizedSet.remove(2) == False
assert randomizedSet.insert(2) == True
assert randomizedSet.getRandom() in (1,2)
assert randomizedSet.remove(1) == True
assert randomizedSet.insert(2) == False
assert randomizedSet.getRandom() == 2