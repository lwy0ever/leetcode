class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * m for _ in range(n)]    # dp[i][j]表示到达[i][j]点的可能路径数
        # 转移方程dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
            