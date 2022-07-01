class MyCalendarThree:
    # 差分数组

    def __init__(self):
        self.pos = list()   # 用于记录日程的起止位置
        self.change = list()   # 用于记录赠/减的预定次数
        self.ansMax = 0

    def book(self, start: int, end: int) -> int:
        p = bisect.bisect_left(self.pos,start)
        if p < len(self.pos):
            if self.pos[p] == start:
                self.change[p] += 1
            else:
                self.pos.insert(p,start)
                self.change.insert(p,1)
        else:
            self.pos.append(start)
            self.change.append(1)
        p2 = bisect.bisect_left(self.pos,end)
        if p2 < len(self.pos):
            if self.pos[p2] == end:
                self.change[p2] -= 1
            else:
                self.pos.insert(p2,end)
                self.change.insert(p2,-1)
        else:
            self.pos.append(end)
            self.change.append(-1)
        #print(p,p2)
        #print(self.pos)
        #print(self.change)

        mx = 0
        t = 0
        for c in self.change[:p2 + 1]:
            t += c
            mx = max(mx,t)
        self.ansMax = max(self.ansMax,mx)
        #print(self.d,self.ansMax)
        return self.ansMax

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)