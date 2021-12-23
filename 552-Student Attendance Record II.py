class Solution:
    def checkRecord(self, n: int) -> int:
        # dp
        # 6种有效状态:
        # A0L0,A0L1,A0L2
        # A1L0,A1L1,A1L2
        # 分别列为dp[0..5]
        dp = [0] * 6
        MOD = 10 ** 9 + 7
        dp[0] = 1
        for _ in range(n):
            newDP = [0] * 6
            # 如果出现P
            newDP[0] = dp[0] + dp[1] + dp[2]
            newDP[3] = dp[3] + dp[4] + dp[5]
            # 如果出现A
            newDP[3] += dp[0] + dp[1] + dp[2]
            # 如果出现L
            newDP[1] = dp[0]
            newDP[2] = dp[1]
            newDP[4] = dp[3]
            newDP[5] = dp[4]
            dp = newDP
            dp[0] = dp[0] % MOD
            dp[3] = dp[3] % MOD
            #print(dp)
        return sum(dp) % MOD