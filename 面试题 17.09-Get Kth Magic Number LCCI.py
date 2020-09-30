class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        p3 = 0
        p5 = 0
        p7 = 0
        dp = [1] * k
        x3 = 3
        x5 = 5
        x7 = 7
        for i in range(1,k):
            dp[i] = min(x3,x5,x7)
            if dp[i] == x3:
                p3 += 1
                x3 = dp[p3] * 3
            if dp[i] == x5:
                p5 += 1
                x5 = dp[p5] * 5
            if dp[i] == x7:
                p7 += 1
                x7 = dp[p7] * 7
        #print(dp)
        return dp[-1]