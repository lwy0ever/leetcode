class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        row = destination[0]
        col = destination[1]
        # 定义preCal[i][j]为i + 1行j + 1列的情况下,路径的数量
        preCal = [[0] * (col + 1) for _ in range(row + 1)]
        preCal[0] = [1] * (col + 1)
        for i in range(1,row + 1):
            preCal[i][0] = 1
            for j in range(1,col + 1):
                preCal[i][j] = preCal[i - 1][j] + preCal[i][j - 1]
        #print(preCal)
        ans = ''
        r = row
        c = col
        #print(r,c)
        counter = 0
        while r > 0 or c > 0:
            if r == 0:
                c -= 1
                ans += 'H'
                continue
            if c == 0:
                r -= 1
                ans += 'V'
                continue
            if preCal[r][c - 1] >= k:   # 水平移动的方案数足够
                c -= 1
                ans += 'H'
            else:   # 水平移动的方案数不够
                ans += 'V'
                k -= preCal[r][c - 1]
                r -= 1
            #print(r,c,ans[-1],k)
        return ans
                