class RecentCounter:

    def __init__(self):
        self.q = []
        self.start = 0
        self.n = 0

    def ping(self, t: int) -> int:
        self.start = bisect.bisect_left(self.q,t - 3000,self.start,self.n)
        self.q.append(t)
        self.n += 1
        return self.n - self.start

    '''
    def __init__(self):
        self.q = []


    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.pop(0)
        return len(self.q)
    '''



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)