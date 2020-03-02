class Solution:
    def countOrders(self, n: int) -> int:
        # 纯数学解法
        # 摆放2n个数字,每个数字出现2次,由于p[i]一定在d[i]之前,所以相同数字前一个是p,有一个是d
        ans = 1
        for i in range(1,n + 1):
            ans = ans * (i * 2) * (i * 2 - 1) // 2
        return ans % (10 ** 9 + 7)
        '''
        # dp解法
        # dp[i][j]表示p了i个,d了j个的方案数
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1,n + 1):
            # 不d的情况下,可以从剩下的(n - i + 1)中随便p一个
            dp[i][0] = dp[i - 1][0] * (n - i + 1)
        for i in range(1,n + 1):
            for j in range(1,n + 1):
                # 要p i个,d j个,可以在dp[i - 1][j]的基础上再p一个,也可以在dp[i][j - 1]的基础上再d一个
                dp[i][j] = dp[i - 1][j] * (n - i + 1) + dp[i][j - 1] * (i - j + 1)
        return dp[-1][-1] % (10 ** 9 + 7)
        '''