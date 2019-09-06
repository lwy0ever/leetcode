class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = [[0] * m for _ in range(n)]
        ans[0][0] = grid[0][0]
        for i in range(1,m):
            ans[0][i] = ans[0][i - 1] + grid[0][i]
        for i in range(1,n):
            ans[i][0] = ans[i - 1][0] + grid[i][0]
        for i in range(1,n):
            for j in range(1,m):
                ans[i][j] = min(ans[i][j - 1],ans[i - 1][j]) + grid[i][j]
        return ans[-1][-1]