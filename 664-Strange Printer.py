class Solution:
    def strangePrinter(self, s: str) -> int:
        # dp[i][j]表示打印s[i:j + 1]需要的次数
        # 如果s[i] == s[j],那么可以在打印s[i]的时候顺便打印s[j],dp[i][j] = dp[i][j - 1]
        # 否则,dp[i][j]等于min(dp[i][k],dp[k + 1][j])
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for length in range(1,n):   # length = 1,表示j = i + 1,实际长度为2
            for i in range(n - length):
                j = i + length
                dp[i][j] = float('inf')
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    for k in range(i,j):
                        dp[i][j] = min(dp[i][j],dp[i][k] + dp[k + 1][j])
        return dp[0][n - 1]