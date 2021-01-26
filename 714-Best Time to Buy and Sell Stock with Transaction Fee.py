class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 优化内存
        n = len(prices)
        stat = [0,-prices[0]]
        for i in range(1,n):
            stat = [max(stat[0],stat[1] + prices[i] - fee),max(stat[1],stat[0] - prices[i])]
        return stat[0]
        
        # dp[i][stat]表示第i天的收益情况,stat=0表示无股票,stat=1表示持有股票
        '''
        n = len(prices)
        dp = [[0,0] for _ in range(n)]
        dp[0] = [0,-prices[0]]
        for i in range(1,n):
            # 保持空仓or卖出
            dp[i][0] = max(dp[i - 1][0],dp[i - 1][1] + prices[i] - fee)
            # 保持持有or买入
            dp[i][1] = max(dp[i - 1][1],dp[i - 1][0] - prices[i])
        return dp[-1][0]
        '''