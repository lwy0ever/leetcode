class Solution:
    def numDecodings(self, s: str) -> int:
        # 考虑s[i]
        # 两种情况
        # 1,只使用s[i]
        # 1.1,如果s[i]是*,dp[i] = dp[i - 1] * 9
        # 1.2,如果s[i]是1-9,dp[i] = dp[i - 1]
        # 1.3,如果s[i]是0,dp[i] = 0
        # 2,使用s[i - 1]和s[i]
        # 2.1,如果s[i - 1]和s[i]都是*,那么可以是11...19,21...26,共15种,dp[i] = dp[i - 2] * 15
        # 2.2,如果s[i - 1]是*
        #   如果s[i]是0...6,则可以是10...16,20...26,dp[i] = dp[i - 2] * 2
        #   如果s[i]是7...9,则可以是17...19,dp[i] = dp[i - 2]
        # 2.3,如果s[i]是*,
        #   如果s[i - 1]是1,*可以是1-9,dp[i] = dp[i - 2] * 9
        #   如果s[i - 1]是2,*可以是1-6,dp[i] = dp[i - 2] * 6
        #   否则dp[i] = 0
        # 2.4,如果s[i - 1]和s[i]都是数字,两者组成的数字是11...26,则dp[i] = dp[i - 2],否则dp[i] = 0
        mod = 10**9 + 7
        a = 0   # 相当于dp[i - 2]
        b = 1   # 相当于dp[i - 1],空字符串是一种方案
        c = 0   # 相当于dp[i]
        n = len(s)
        
        def check1(c):
            if c == '*':
                return 9
            elif c == '0':
                return 0
            else:
                return 1
        
        def check2(c1,c2):
            if c1 == '*':
                if c2 == '*':
                    return 15
                elif '0' <= c2 <= '6':
                    return 2
                else:
                    return 1
            if c2 == '*':
                if c1 == '1':
                    return 9
                elif c1 == '2':
                    return 6
                else:
                    return 0
            v = int(c1) * 10 + int(c2)
            if 10 <= v <= 26:
                return 1
            else:
                return 0

        for i in range(n):
            # 只使用s[i]
            c = b * check1(s[i])
            # 使用s[i - 1]和s[i]
            if i > 0:
                c += a * check2(s[i - 1],s[i])
            c %= mod
            a = b
            b = c
        return c        