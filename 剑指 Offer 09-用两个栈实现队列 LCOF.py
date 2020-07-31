class CQueue:

    def __init__(self):
        self.head = []  # 队列前半部分,倒序
        self.tail = []  # 队列后半部分,正序


    def appendTail(self, value: int) -> None:
        self.tail.append(value)


    def deleteHead(self) -> int:
        if self.head:
            return self.head.pop()
        while self.tail:
            self.head.append(self.tail.pop())
        return self.head.pop() if self.head else -1



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()