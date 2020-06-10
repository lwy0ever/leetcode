class SortedStack:

    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        tmp = []
        while self.data and val > self.data[-1]:
            tmp.append(self.data.pop())
        self.data.append(val)
        while tmp:
            self.data.append(tmp.pop())
        #print(self.data)


    def pop(self) -> None:
        if self.isEmpty():
            return
        self.data.pop()


    def peek(self) -> int:
        #print(self.data)
        if self.isEmpty():
            return -1
        return self.data[-1]


    def isEmpty(self) -> bool:
        #print(self.data)
        return len(self.data) == 0



# Your SortedStack object will be instantiated and called as such:
# obj = SortedStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.peek()
# param_4 = obj.isEmpty()