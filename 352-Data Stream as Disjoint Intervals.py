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
        # 如果pos & 1 == 1,说明在区间内,不需要处理
        # 如果pos & 1 == 0,说明在右侧的区间外
        if pos & 1 == 0:
            # 如果挨着右侧区间,则扩展右侧区间
            if pos < self.n and self.dt[pos] - val == 1:
                self.dt[pos] = val
            else:   # 如果不挨着右侧区间,则新插入区间
                self.dt.insert(pos,val)
                self.dt.insert(pos,val)
                self.n += 2
            # 如果又挨上了左侧区间,则合并
            if pos > 0 and self.dt[pos] - self.dt[pos - 1] <= 1:
                self.dt.pop(pos)
                self.dt.pop(pos - 1)
                self.n -= 2

    def getIntervals(self) -> List[List[int]]:
        # 拼接成需要的答案形式
        return [*zip(self.dt[:: 2], self.dt[1:: 2])]


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()