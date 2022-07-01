class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = nums
        self.k = k
        heapq.heapify(self.h)
        while len(self.h) > k:
            heapq.heappop(self.h)

    def add(self, val: int) -> int:
        if len(self.h) == self.k:
            if val > self.h[0]:
                heapq.heapreplace(self.h,val)
        else:
            heapq.heappush(self.h,val)
        return self.h[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)