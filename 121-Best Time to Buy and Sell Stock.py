class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # you were only permitted to complete at most one transaction
        
        # dp[i][j][k]表示第i天，至今最多进行过j次买卖时的盈利情况，k=0表示没有股票，k=1表示持有股票
        n = len(prices)
        if n == 0:
          return 0
        K = 1   #最多交易次数
        dp = [[[0,0] for j in range(K + 1)] for i in range(n)]
        for j in range(K,0,-1):
            dp[0][j][0] = 0
            dp[0][j][1] = -prices[0]
        for i in range(1,n):
            for j in range(K,0,-1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])   # 保持没有股票状态or卖掉股票
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j - 1][0] - prices[i])   # 保持持有股票状态or买入股票
        #print(dp)
        return dp[-1][-1][0] # dp[-1][0][0] 一定大于 dp[-1][0][1]
        '''
        n = len(prices)
        if n <= 1:
            return 0
        mi = prices[0]
        ma = 0
        for i in range(1,n):
            # 记录【今天之前买入的最小值】
            mi = min(prices[i],mi)
            #计算【今天之前最小值买入，今天卖出的获利】，也即【今天卖出的最大获利】
            #比较【每天的最大获利】，取最大值即可
            ma = max(ma,prices[i] - mi)
        return ma
        '''