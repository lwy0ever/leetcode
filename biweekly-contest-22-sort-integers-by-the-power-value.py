class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        self.l = {1:0}
        arr = [[i,0] for i in range(lo,hi + 1)]
        
        def cal(x):
            if x in self.l:
                return self.l[x]
            if x & 1 == 0:
                self.l[x] = cal(x // 2) + 1
                return self.l[x]
            else:
                self.l[x] = cal(x * 3 + 1) + 1
                return self.l[x]

        for i in range(lo,hi + 1):
            arr[i - lo][1] = cal(i)
        arr.sort(key = lambda x:(x[1],x[0]))
        return arr[k - 1][0]