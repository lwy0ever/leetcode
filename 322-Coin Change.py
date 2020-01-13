class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [float('inf')] * (amount + 1)  # dp[i]表示i可以被最少多少个coins组成
        dp[0] = 0
        for c in coins:
            for i in range(c,amount + 1):
                dp[i] = min(dp[i],dp[i - c] + 1)
        return -1 if dp[-1] == float('inf') else dp[-1]