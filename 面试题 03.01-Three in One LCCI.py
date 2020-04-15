class TripleInOne:

    def __init__(self, stackSize: int):
        n = 3
        self.size = stackSize
        self.s = [0] * stackSize * n
        self.cur = []   # 指针,指向当前为空的元素
        for i in range(n):
            self.cur.append(stackSize * i)

    def push(self, stackNum: int, value: int) -> None:
        if self.cur[stackNum] == (stackNum + 1) * self.size:    # 栈满了
            return
        else:
            self.s[self.cur[stackNum]] = value
            self.cur[stackNum] += 1


    def pop(self, stackNum: int) -> int:
        if self.cur[stackNum] == stackNum * self.size:  # 栈为空
            return -1
        else:
            self.cur[stackNum] -= 1
            return self.s[self.cur[stackNum]]

    def peek(self, stackNum: int) -> int:
        if self.cur[stackNum] == stackNum * self.size:  # 栈为空
            return -1
        else:
            return self.s[self.cur[stackNum] - 1]


    def isEmpty(self, stackNum: int) -> bool:
        return self.cur[stackNum] == stackNum * self.size   # 栈为空


# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)