class StackOfPlates:

    def __init__(self, cap: int):
        self.cap = cap
        self.data = [[]]

    def push(self, val: int) -> None:
        if self.cap == 0:
            return
        if len(self.data[-1]) == self.cap:
            self.data.append([])
        self.data[-1].append(val)

    def pop(self) -> int:
        if self.cap == 0:
            return -1
        if self.data[-1]:
            r = self.data[-1].pop()
            if not self.data[-1]:
                self.data.pop()
            if not self.data:
                self.data.append([])
            return r
        else:
            return -1

    def popAt(self, index: int) -> int:
        if self.cap == 0:
            return -1
        #print(self.data)
        if len(self.data) > index and self.data[index]:
            r = self.data[index].pop()
            if not self.data[index]:
                self.data.pop(index)
            if not self.data:
                self.data.append([])
            return r
        else:
            return -1



# Your StackOfPlates object will be instantiated and called as such:
# obj = StackOfPlates(cap)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAt(index)