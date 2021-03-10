class Solution:
    def minDays(self, n: int) -> int:
        # n个橘子,经过1天,可以变成
        # 1,n - 1
        # 2,n // 2
        # 3,n // 3
        # 显然,方法2,3比方法1要快
        dp = dict()  # dp[i]表示吃i个橘子需要的天数
        dp[0] = 0
        dp[1] = 1
        def helper(d):
            if d in dp:
                return dp[d]
            d3,m3 = divmod(d,3)
            helper(d3)
            d2,m2 = divmod(d,2)
            helper(d2)
            dp[d] = min(dp[d3] + m3,dp[d2] + m2) + 1
            #print(d,dp[d])
            #return dp[d]
        helper(n)
        #print(dp)
        return dp[n]
    '''
    @lru_cache(None)
    def minDays(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 0
        return min(self.minDays(n // 3) + n % 3,self.minDays(n // 2) + n % 2) + 1
    '''