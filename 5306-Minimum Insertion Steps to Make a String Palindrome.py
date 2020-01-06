class Solution:
    def minInsertions(self, s: str) -> int:
        # https://blog.csdn.net/qq_41890797/article/details/87490945
        # 因为只能添加字符，所以我们可以在创建一个和原子符串（s）相反的字符串（t）,当字符串为回文串的时候 ，s == t
        # 又因为只能添加字符，所以需要添加的个数就是 ：原字符串的的长度 l - s 和 t 的最长公共子序列的长度
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]  # dp[i][j]表示s[:i]和t[:j]的最大公共字符串长度
        t = s[::-1] # s的倒序
        for i in range(n):
            for j in range(n):
                if s[i] == t[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1],dp[i + 1][j])
        return n - dp[n][n]