class RandomizedSet:

    def __init__(self):
        self.set = {}    

    def insert(self, val: int) -> bool:
        exist = val not in self.set
        self.set[val] = True
        return exist

    def remove(self, val: int) -> bool:
        exist = val in self.set
        if exist:
            del self.set[val]
        return exist

    def getRandom(self) -> int:
        return random.choice(list(self.set.keys()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
