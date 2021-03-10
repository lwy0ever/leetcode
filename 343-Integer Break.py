class Solution:
    def integerBreak(self, n: int) -> int:
        # dp算法
        dp = [1] * n    # dp[i]表示i + 1的最大化乘积
        for i in range(1,n):
            for j in range(1,i + 1):
                #print(i + 1,j,i - j + 1,dp[i - j])
                dp[i] = max(dp[i],dp[i - j] * j,(i - j + 1) * j)
        #print(dp)
        return dp[-1]
        # 数学算法
        '''
        # 3 * 3 > 2 * 2 * 2
        base = {2:1,3:2,4:4,5:6}
        if n in base:
            return base[n]
        # n >= 6
        d,m = divmod(n - 3,3)
        ans = 3 ** d
        ans *= max(base[m + 3],m + 3)
        return ans
        '''