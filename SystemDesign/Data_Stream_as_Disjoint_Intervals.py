class SummaryRanges:
    def __init__(self):
        self.stream = []

    def addNum(self, value: int) -> None:
        self.stream.append(value)
        self.stream.sort()

    def getIntervals(self) -> List[List[int]]:
        if len(self.stream) <= 0:
            return []
        res = []
        curr =[self.stream[0],self.stream[0]]
        last = self.stream[0]
        for i in self.stream:
            if i - last > 1:
                res.append(curr)
                curr = [i,i]
            else:
                curr[1]=i
            last = i
        res.append(curr)
        return res

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
