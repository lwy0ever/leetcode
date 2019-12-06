class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        # 由于只有push和pop操作,利用stackMin存放最小值
        self.stackMin = []
        #self.sorted = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.stackMin and x > self.stackMin[-1]:
            self.stackMin.append(self.stackMin[-1])
        else:
            self.stackMin.append(x)
        #bisect.insort(self.sorted,x)

    def pop(self) -> None:
        self.stackMin.pop()
        return self.stack.pop()
        #pos = bisect.bisect(self.sorted,p)
        #self.sorted.pop(pos - 1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stackMin[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()