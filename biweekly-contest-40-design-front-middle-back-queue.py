class FrontMiddleBackQueue:

    # 如果使用list,pop时的效率太低了
    # 可以使用两个deque实现
    # 保持left == right或者left == right + 1
    def __init__(self):
        self.left = deque()
        self.leftlen = 0
        self.right = deque()
        self.rightlen = 0

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        if self.leftlen > self.rightlen:    # 不平衡
            self.right.appendleft(self.left.pop())
            self.rightlen += 1
        else:
            self.leftlen += 1
        #print(self.left,self.leftlen,self.right,self.rightlen)

    def pushMiddle(self, val: int) -> None:
        if self.leftlen > self.rightlen:    # 不平衡
            self.right.appendleft(self.left.pop())
            self.left.append(val)
            self.rightlen += 1
        else:
            self.left.append(val)
            self.leftlen += 1
        #print(self.left,self.leftlen,self.right,self.rightlen)

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        if self.leftlen > self.rightlen:    # 不平衡
            self.rightlen += 1
        else:
            self.left.append(self.right.popleft())
            self.leftlen += 1
        #print(self.left,self.leftlen,self.right,self.rightlen)

    def popFront(self) -> int:
        if self.leftlen == 0:
            return -1
        if self.leftlen > self.rightlen:
            self.leftlen -= 1
        else:
            self.left.append(self.right.popleft())
            self.rightlen -= 1
        #print(self.left,self.leftlen,self.right,self.rightlen)
        return self.left.popleft()

    def popMiddle(self) -> int:
        if self.leftlen == 0:
            return -1
        if self.leftlen > self.rightlen:
            self.leftlen -= 1
            #print(self.left,self.leftlen,self.right,self.rightlen)
            return self.left.pop()
        else:
            self.rightlen -= 1
            ans = self.left.pop()
            self.left.append(self.right.popleft())
            #print(self.left,self.leftlen,self.right,self.rightlen)
            return ans

    def popBack(self) -> int:
        if self.leftlen == 0:
            return -1

        if self.leftlen > self.rightlen:
            self.right.appendleft(self.left.pop())
            self.leftlen -= 1
        else:
            self.rightlen -= 1
        #print(self.left,self.leftlen,self.right,self.rightlen)
        return self.right.pop()


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()