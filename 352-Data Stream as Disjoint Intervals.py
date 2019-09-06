from bisect import bisect,insort
class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dt = []
        self.n = 0

    def addNum(self, val: int) -> None:
        pos = bisect(self.dt,val)
        #print(val,pos,self.dt)
        if pos % 2 == 0:
            if pos < self.n and self.dt[pos] - val == 1:
                self.dt[pos] = val
            else:
                self.dt.insert(pos,val)
                self.dt.insert(pos,val)
                self.n += 2
            if pos > 0 and self.dt[pos] - self.dt[pos - 1] <= 1:
                self.dt.pop(pos)
                self.dt.pop(pos - 1)
                self.n -= 2

    def getIntervals(self) -> List[List[int]]:
        return [*zip(self.dt[:: 2], self.dt[1:: 2])]


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()