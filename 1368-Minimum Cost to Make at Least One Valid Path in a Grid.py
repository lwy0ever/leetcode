class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                dp[i][j] = m * n
        dp[0][0] = 0
        fromP = {(0,0)}
        di = [(0,1),(0,-1),(1,0),(-1,0)]
        # 类似bfs
        while fromP:
            toP = set()
            #print(fromP)
            for f in fromP:
                #print(f)
                if 1 <= grid[f[0]][f[1]] <= 4:
                    ni = f[0] + di[grid[f[0]][f[1]] - 1][0]
                    mi = f[1] + di[grid[f[0]][f[1]] - 1][1]
                    if 0 <= ni < n and 0 <= mi < m:
                        if dp[ni][mi] > dp[f[0]][f[1]]:
                            toP.add((ni,mi))
                            dp[ni][mi] = dp[f[0]][f[1]]
                for d in di:
                    ni = f[0] + d[0]
                    mi = f[1] + d[1]
                    if 0 <= ni < n and 0 <= mi < m:
                        if dp[ni][mi] > dp[f[0]][f[1]] + 1:
                            toP.add((ni,mi))
                            dp[ni][mi] = dp[f[0]][f[1]] + 1
            fromP = toP
            #print(dp)
        return dp[-1][-1]
