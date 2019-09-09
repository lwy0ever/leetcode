class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp(i,j)表示s[i:] 和 p[j:] 是否能匹配
        # 采用从后向前的方法可以避免递归
        ns = len(s)
        np = len(p)
        dp = [[False] * (np + 1) for _ in range(ns + 1)]
        dp[-1][-1] = True
        for i in range(ns,-1,-1):
            for j in range(np - 1,-1,-1):
                match = i < ns and p[j] in (s[i],'.')
                if j + 1 < np and p[j + 1] == '*':
                    dp[i][j] = match and dp[i + 1][j] or dp[i][j + 2]
                else:
                    dp[i][j] = match and dp[i + 1][j + 1]
        return dp[0][0]        