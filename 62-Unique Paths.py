class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 优化空间的基本算法
        dp = [1] * m    # dp[i]表示某一行到达i点的可能路径数
        # 转移方程dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        for i in range(1,n):
            dp[0] = 1
            for j in range(1,m):
                dp[j] += dp[j - 1]
        return dp[-1]

        '''
        # 基本算法
        dp = [[1] * m for _ in range(n)]    # dp[i][j]表示到达[i][j]点的可能路径数
        # 转移方程dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
        '''