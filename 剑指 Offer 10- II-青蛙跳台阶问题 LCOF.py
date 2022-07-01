class Solution:
    def numWays(self, n: int) -> int:
        # dp
        if n < 2:
            return 1
        dp = [0] * n # 从-1开始,跳到n - 1
        dp[0] = 1
        dp[1] = 2   # 可以是1 + 1,也可以是2
        for i in range(2,n):
            dp[i] = (dp[i - 2] + dp[i - 1]) % (10 ** 9 + 7)
        return dp[-1]