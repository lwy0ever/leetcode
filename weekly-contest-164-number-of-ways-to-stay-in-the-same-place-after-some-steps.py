class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        if arrLen == 1:
            return 1
        m = 10 ** 9 + 7
        # dp[i]表示走到位置i的方案数量
        dp = [0] * min(steps + 1,arrLen)
        dp[0] = 1
        for _ in range(steps):
            # ndp[i]表示再走1步的情况下,走到位置i的方案数量
            ndp = [0] * min(steps + 1,arrLen)
            ndp[0] = (dp[0] + dp[1]) % m
            for i in range(1,min(steps + 1,arrLen) - 1):
                ndp[i] = (dp[i - 1] + dp[i] + dp[i + 1]) % m
            ndp[-1] = (dp[-2] + dp[-1]) % m
            dp = ndp
            #print(dp)
        return dp[0]