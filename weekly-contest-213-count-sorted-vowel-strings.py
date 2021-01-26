class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[1] * 5 for _ in range(n)]    # dp[i][j]表示用第j个字母(a,e,i,o,u)组成第i位时的方案数
        for i in range(1,n):
            for j in range(1,5):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return sum(dp[-1])