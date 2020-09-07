class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        # dp = [0] * 26
        # dp[i]表示以chr(ord('a') + i)为结尾的字符串,包含的子串的数量
        if not p: return 0
        dp = [0] * 26
        base = ord('a')
        dp[ord(p[0]) - base] = 1
        preLen = 1
        for i in range(1,len(p)):
            if ord(p[i]) - ord(p[i - 1]) in (1,-25):  # 连续或者是za形式
                preLen += 1
            else:   # 不连续
                preLen = 1
            dp[ord(p[i]) - base] = max(dp[ord(p[i]) - base],preLen) # 这样可以对字符串去重
            #dp[ord(p[i]) - base] += preLen    # 这个是不去重的算法
            #print(dp)
        return sum(dp)