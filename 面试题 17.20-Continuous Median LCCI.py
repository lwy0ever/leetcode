class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = [] # 先插入small
        self.large = [] # 存储元素的负值
        self.cnt = 0    # 0表示偶数个元素,1表示奇数个


    def addNum(self, num: int) -> None:
        self.cnt ^= 1
        if self.cnt:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
        else:
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        #print(self.small,self.large)


    def findMedian(self) -> float:
        if self.cnt:
            return -self.small[0]
        else:
            return (self.large[0] - self.small[0]) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()