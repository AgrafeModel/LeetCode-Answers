# not fast at all
class AllOne:

    def __init__(self):
        self.data = {}
        
    def inc(self, key: str) -> None:
        if key in self.data:
            self.data[key]+=1
        else:
            self.data[key]=1

    def dec(self, key: str) -> None:
       if key in self.data:
        self.data[key]-=1
        if self.data[key] <= 0:
            self.data.pop(key)
             

    def getMaxKey(self) -> str:
        if not self.data:
            return ""
        
        mx = max(self.data.values())
        for key in self.data.keys():
            if self.data[key] == mx:
                return key
    
    def getMinKey(self) -> str:
        if not self.data:
            return ""

        mn = min(self.data.values())
        for key in self.data.keys():
            if self.data[key] == mn:
                return key    


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
