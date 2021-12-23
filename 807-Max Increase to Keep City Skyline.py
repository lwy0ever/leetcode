class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maxM = [0] * m  # 记录每行的最高值
        maxN = [0] * n  # 记录每列的最高值
        for i in range(m):
            for j in range(n):
                maxM[i] = max(maxM[i],grid[i][j])
                maxN[j] = max(maxN[j],grid[i][j])
        ans = 0
        for i in range(m):
            for j in range(n):
                ans += min(maxM[i],maxN[j]) - grid[i][j]
        return ans