class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][j][k]表示第i天，至今最多进行过j次买卖时的盈利情况，k=0表示没有股票，k=1表示持有股票
        n = len(prices)
        if n == 0:
            return 0
        #K = 1   #最多交易次数
        # K = float('inf')
        # dp = [[[0,0] for j in range(K + 1)] for i in range(n)]
        dp = [[0,0] for i in range(n)]
        #for j in range(K,0,-1):
        #    dp[0][j][0] = 0
        #    dp[0][j][1] = -prices[0]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        #for i in range(1,n):
        #    for j in range(K,0,-1):
        #        dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])   # 保持没有股票状态or卖掉股票
        #        dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j - 1][0] - prices[i])   # 保持持有股票状态or买入股票
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0] - prices[i])
        #print(dp)
        #return dp[-1][-1][0] # dp[-1][0][0] 一定大于 dp[-1][0][1]
        return dp[-1][0]