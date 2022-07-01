class DetectSquares:

    def __init__(self):
        # 如果形成轴对齐正方形,需要两个顶点的x1 - y1 = x2 - y2或者x1 + y1 = x2 + y2
        # 保存x - y,x + y
        # disA[x - y] = {x1:cnt,x2:cnt,x3:cnt,...]
        # disB[x + y] = {x1:cnt,x2:cnt,x3:cnt,...]
        self.disA = dict()
        self.disB = dict()
        self.points = collections.defaultdict(int)


    def add(self, point: List[int]) -> None:
        x,y = point
        if x - y in self.disA:
            self.disA[x - y][x] += 1
        else:
            self.disA[x - y] = collections.defaultdict(int)
            self.disA[x - y][x] = 1
        if x + y in self.disB:
            self.disB[x + y][x] += 1
        else:
            self.disB[x + y] = collections.defaultdict(int)
            self.disB[x + y][x] = 1
        self.points[(x,y)] += 1
        #print(self.dis)
        #print(self.points)


    def count(self, point: List[int]) -> int:
        ans = 0
        x,y = point
        if x - y in self.disA:
            #print(self.disA[x - y])
            for k,v in self.disA[x - y].items():
                if k == x:  # 点重合
                    continue
                ans += v * self.points[(k,y)] * self.points[(x,k - (x - y))]
        if x + y in self.disB:
            #print(self.disB[x + y])
            for k,v in self.disB[x + y].items():
                if k == x:  # 点重合
                    continue
                ans += v * self.points[(k,y)] * self.points[(x,(x + y) - k)]
        return ans



# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)