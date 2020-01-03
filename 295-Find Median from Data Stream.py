class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.cnt = 0
        self.max_heap = []  # 大顶堆
        self.min_heap = []  # 小顶堆

    def addNum(self, num: int) -> None:
        self.cnt += 1
        # 使用heapq
        # 由于python中的堆都是小顶堆,所以在max_heap中,保存的是-val
        # 数据为奇数个的情况下,优先存在小顶堆
        if self.cnt & 1 == 0:
            if self.min_heap and num > self.min_heap[0]:
                heapq.heappush(self.min_heap,num)
                t = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap,-t)
            else:
                heapq.heappush(self.max_heap,-num)
        else:
            if self.min_heap and num < self.min_heap[0]:
                heapq.heappush(self.max_heap,-num)
                t = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap,-t)
            else:
                heapq.heappush(self.min_heap,num)
        '''
        heapq.heappush(self.max_heap,-num)
        t = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap,-t)
        if self.cnt & 1 == 0:
            t = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,-t)
        '''

    def findMedian(self) -> float:
        if self.cnt & 1:
            return self.min_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()