class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        # dp
        # 由于要求 非空子串 唯一
        # 定义dp[c]为以字符c结尾,最长的非空字串长度(以c结尾的长度=以c结尾的非空字串数量)
        dp = defaultdict(int)
        n = len(p)
        k = 1
        dp[p[0]] = 1
        for i in range(1,n):
            if ord(p[i]) - ord(p[i - 1]) in (1,-25):    # 连续
                k += 1
            else:
                k = 1
            dp[p[i]] = max(dp[p[i]],k)
            #print(dp)
        return sum(dp.values())