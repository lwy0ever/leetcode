class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # dp
        n = len(s)
        # dp[i][j]表示字符串s[i:j + 1]的最长回文子序列
        dp = [[0] * n for _ in range(n)]
        for l in range(n - 1,-1,-1):    # l从n-1倒序,这样可以保证每个子问题都被提前计算好了
            dp[l][l] = 1
            for r in range(l + 1,n):
                if s[l] == s[r]:
                    dp[l][r] = dp[l + 1][r - 1] + 2
                else:
                    dp[l][r] = max(dp[l + 1][r],dp[l][r - 1])
        return dp[0][n - 1]