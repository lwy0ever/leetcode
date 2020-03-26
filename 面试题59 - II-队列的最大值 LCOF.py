class MaxQueue:

    def __init__(self):
        self.q = [] # 按顺序存放数据
        self.m = [] # 存放最大值,最大值放在m[0]

    def max_value(self) -> int:
        return self.m[0] if self.m else -1


    def push_back(self, value: int) -> None:
        self.q.append(value)
        while self.m and self.m[-1] < value:
            self.m.pop()
        self.m.append(value)


    def pop_front(self) -> int:
        if not self.q:
            return -1
        if self.q[0] == self.m[0]:
            self.m.pop(0)
        return self.q.pop(0)


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()