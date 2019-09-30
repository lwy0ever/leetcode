class DinnerPlates:

    def __init__(self, capacity: int):
        self.p = [[]]
        self.cur = 0
        self.deep = capacity

    def push(self, val: int) -> None:
        self.p[self.cur].append(val)
        while len(self.p[self.cur]) == self.deep:
            self.cur += 1
            if len(self.p) < self.cur + 1:
                self.p.append([])
        #print(self.p)

    def pop(self) -> int:
        cc = len(self.p) - 1
        while cc >= 0 and not self.p[cc]:
            self.p.pop()
            cc -= 1
        if cc >= 0:
            res = self.p[cc].pop()
            cur = cc
            return res
        else:
            return -1

    def popAtStack(self, index: int) -> int:
        if self.p[index]:
            res = self.p[index].pop()
            if self.cur > index:
                self.cur = index
            return res
        else:
            return -1
        


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)