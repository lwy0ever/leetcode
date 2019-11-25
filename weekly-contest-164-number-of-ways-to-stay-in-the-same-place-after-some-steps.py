class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        if arrLen == 1:
            return 1
        dp = [0] * min(steps + 1,arrLen)
        dp[0] = 1
        for _ in range(steps):
            ndp = [0] * min(steps + 1,arrLen)
            ndp[0] = dp[0] + dp[1]
            for i in range(1,min(steps + 1,arrLen) - 1):
                ndp[i] = dp[i - 1] + dp[i] + dp[i + 1]
            ndp[-1] = dp[-2] + dp[-1]
            dp = ndp
            #print(dp)
        return dp[0] % (10 ** 9 + 7)