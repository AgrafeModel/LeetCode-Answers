class RandomizedCollection:

    def __init__(self):
        self.data = []

    def insert(self, val: int) -> bool:
        exist = (val in self.data)
        self.data.append(val)
        return not exist

    def remove(self, val: int) -> bool:
        if val not in self.data:
            return False
        
        self.data.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)



# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
