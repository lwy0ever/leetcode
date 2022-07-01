class Solution:

    def __init__(self, rects: List[List[int]]):
        # 还好，所有的矩形不重叠
        # 前缀和 + 二分查找
        # 矩形内（包括边）包括的点的数量 / 总数量 = 该矩形被选中的概率
        self.rate = [0]
        for a,b,x,y in rects:
            self.rate.append(self.rate[-1] + (x + 1 - a) * (y + 1 - b))
        self.rate.pop(0)
        self.total = self.rate[-1]
        self.rects = rects
        #print(self.rate)
        #print(self.rects)

    def pick(self) -> List[int]:
        r = randint(0,self.total - 1)    # randint(a,b)返回区间[a,b]
        i = bisect.bisect_right(self.rate,r)
        a,b,x,y = self.rects[i]
        return [random.randint(a,x),random.randint(b,y)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()