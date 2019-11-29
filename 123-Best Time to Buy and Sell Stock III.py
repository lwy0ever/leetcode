class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 超简单状态
        n = len(prices)
        if n == 0:
            return 0
        s1 = -prices[0]     # 表示满仓,买过过1次的收益情况
        s2 = float('-inf')  # 表示空仓,买入过1次的收益情况
        s3 = float('-inf')  # 表示满仓,买入过2次的收益情况
        s4 = float('-inf')  # 表示空仓,买入过2次的收益情况
        for i in range(1,n):
            s1 = max(s1,-prices[i])
            s2 = max(s2,s1 + prices[i])
            s3 = max(s3,s2 - prices[i])
            s4 = max(s4,s3 + prices[i])
        return max(0,s4)
        '''
        # dp[i][j][k]表示在第i天,进行过j次买入交易的盈利情况(j的范围是[0,2]).k = 0表示没有股票,k = 1表示持有股票
        n = len(prices)
        if n == 0:
            return 0
        dp = [[[0] * 2 for _ in range(2 + 1)] for _ in range(n)]
        dp[0][0][0] = 0
        for j in range(1,2 + 1):
            dp[0][j][1] = -prices[0]
        for i in range(1,n):
            for j in range(1,2 + 1):
                dp[i][j][0] = max(dp[i - 1][j][0],dp[i - 1][j][1] + prices[i]) # 不买股票or卖出股票
                dp[i][j][1] = max(dp[i - 1][j][1],dp[i - 1][j - 1][0] - prices[i]) # 继续持有or买入股票
        #print(dp)
        return dp[-1][-1][0]    # 最后空仓一定比持有收益大(dp[-1][-1][0] >= dp[-1][-1][1])
        '''