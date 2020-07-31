class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.cnt = 0
        self.left = []  # 从小到大
        self.right = [] # 需要从大到小,因此存放-val


    def addNum(self, num: int) -> None:
        # 数据量为单数时,优先存在left
        self.cnt += 1
        if self.cnt & 1:
            if self.right and num > -self.right[-1]:    # 放在右边
                bisect.insort(self.left,-self.right.pop())
                bisect.insort(self.right,-num)
            else:   # 放在左边
                bisect.insort(self.left,num)
        else:
            if self.left and num < self.left[-1]:    # 放在左边
                bisect.insort(self.right,-self.left.pop())
                bisect.insort(self.left,num)
            else:   # 放在右边
                bisect.insort(self.right,-num)
        #print(self.left,self.right)

    def findMedian(self) -> float:
        if self.cnt & 1:
            return self.left[-1] / 1
        else:
            return (self.left[-1] - self.right[-1]) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()