class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [[0] * (m + 1) for _ in range(n + 1)]    # dp[i][j]表示可以组成t[:i + 1]的s[:j + 1]的子序列的个数
        # 如果t == '',则可能性永远是1
        for i in range(m + 1):
            dp[0][i] = 1
        for i in range(1,n + 1):
            for j in range(1,m + 1):
                if t[i - 1] == s[j - 1]:
                    # 如果t[i - 1] == s[j - 1]
                    # 那么可以直接使用dp[i][j - 1](不使用s[j - 1])
                    # 也可以使用dp[i - 1][j - 1](使用s[j - 1])
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
                else:
                    # 只能使用dp[i][j - 1](不使用s[j - 1])
                    dp[i][j] = dp[i][j - 1]
        #print('\n'.join(map(str,dp)))
        return dp[n][m]