class Solution:
    def numDecodings(self, s: str) -> int:
        if s == '' or s[0] == '0':
            return 0
        n = len(s)
        dp = [1] * (n + 1)   # dp[i]表示s[:i]的decode方法数
        for i in range(1,n):
            if 1 <= int(s[i]) <= 9:
                if 11 <= int(s[i - 1:i + 1]) <= 19 or 21 <= int(s[i - 1:i + 1]) <= 26:
                    dp[i + 1] = dp[i - 1] + dp[i]
                else:
                    dp[i + 1] = dp[i]
            else:   # s[i] == '0'
                if s[i - 1] in ('1','2'):
                    dp[i + 1] = dp[i - 1]
                else:
                    return 0
        #print(dp)
        return dp[-1]