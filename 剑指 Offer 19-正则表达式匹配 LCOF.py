class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ns = len(s)
        np = len(p)
        dp = [[False] * (np + 1) for _ in range(ns + 1)]  # dp[i][j]表示s[:i]和p[:j]是否匹配
        
        def matches(i,j):   # 匹配s[i - 1]和p[j - 1]
            if i == 0:
                return False
            return p[j - 1] == '.' or s[i - 1] == p[j - 1] 

        dp[0][0] = True
        for i in range(ns + 1):
            for j in range(1,np + 1):
                if p[j - 1] == '*':
                    dp[i][j] |= dp[i][j - 2]    # *匹配0次
                    if matches(i, j - 1):
                        dp[i][j] |= dp[i - 1][j]    # *匹配1次及以上
                else:
                    if matches(i, j):
                        dp[i][j] |= dp[i - 1][j - 1]
        #print(dp)
        return dp[ns][np]