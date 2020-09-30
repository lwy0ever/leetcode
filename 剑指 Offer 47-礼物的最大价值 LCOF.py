class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        # dp
        # 逐行考虑
        m = len(grid)
        n = len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]
        for i in range(1,n):
            dp[i] = dp[i - 1] + grid[0][i]
        for r in range(1,m):
            dp[0] += grid[r][0]
            for i in range(1,n):
                dp[i] = max(dp[i - 1],dp[i]) + grid[r][i]
        return dp[-1]