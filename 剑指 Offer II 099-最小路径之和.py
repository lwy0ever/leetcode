class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 每次只能向下or向右
        # dp
        m = len(grid)
        n = len(grid[0])
        ansPre = [float('inf')] * n
        ansPre[0] = 0
        ans = [float('inf')] * n
        for i in range(m):
            ans[0] = ansPre[0] + grid[i][0]
            for j in range(1,n):
                ans[j] = min(ans[j - 1],ansPre[j]) + grid[i][j]
                #print(ansPre)
                #print(ans)
            #print(ansPre)
            #print(ans)
            ansPre = ans
            ans = [float('inf')] * n
        return ansPre[-1]