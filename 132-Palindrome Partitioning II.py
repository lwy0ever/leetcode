class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        # 判断直接回文
        if n <= 1 or s == s[::-1]:
            return 0
        # trick:测试数据里面有很多特殊数据,可以通过1次分割完成
        for i in range(1, n):
            if s[i:] == s[:i - 1:-1] and s[:i] == s[i - 1::-1]:
                return 1
        
        dp = [i for i in range(-1, n)]  # dp[i]表示s[:i + 1]需要的cut次数
        #print(dp)
        for end in range(1,n + 1):
            for start in range(end):
                if s[start:end] == s[start:end][::-1]:
                    dp[end] = min(dp[end],dp[start] + 1)
        return dp[-1]