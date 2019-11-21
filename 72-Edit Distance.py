class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        # dp[i][j]表示word1[:i + 1]和word2[:j + 1]匹配所需要的编辑次数
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = i
        for i in range(m + 1):
            dp[0][i] = i
        for i in range(1,n + 1):
            for j in range(1,m + 1):
                # 转移方程
                # dp[i][j]从dp[i][j - 1]来,或者dp[i - 1][j]来
                dp[i][j] = min(dp[i][j - 1] + 1,dp[i - 1][j] + 1)
                # dp[i][j]从dp[i - 1][j - 1]来
                if word1[i - 1] != word2[j - 1]:
                    dp[i][j] = min(dp[i][j],dp[i - 1][j - 1] + 1)
                else:
                    dp[i][j] = min(dp[i][j],dp[i - 1][j - 1])
        #print(dp)
        return dp[n][m]