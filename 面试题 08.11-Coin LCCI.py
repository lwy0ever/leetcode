class Solution:
    def waysToChange(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        coins = [25,10,5,1] # 先考虑面值较大的
        for c in coins:
            for i in range(c,n + 1):
                dp[i] += dp[i - c]
            #print(dp)
        return dp[-1] % (10 ** 9 + 7)