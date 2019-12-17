class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        infinity = False
        if k > n // 2:
            k = 1
            infinity = True
        mi = -sum(prices)
        dp0 = [[0] * n for _ in range(k + 1)] # dp0[i][j]表示第j天,i次交易后,空仓最大收益.交易计数以买入为准
        dp1 = [[0] * n for _ in range(k + 1)] # dp1[i][j]表示第j天,i次交易后,满仓最大收益
        for i in range(k + 1):
            dp0[i][0] = 0
            dp1[i][0] = -prices[0]
        for j in range(1,n):
            for i in range(k,0,-1): # 要倒序,避免一天多次交易
                if infinity:
                    dp0[i][j] = max(dp0[i][j - 1],dp1[i][j - 1] + prices[j])    # 保持空仓or卖出
                    dp1[i][j] = max(dp1[i][j - 1],dp0[i][j - 1] - prices[j])  # 保持满仓or买入
                else:
                    dp0[i][j] = max(dp0[i][j - 1],dp1[i][j - 1] + prices[j])    # 保持空仓or卖出
                    dp1[i][j] = max(dp1[i][j - 1],dp0[i - 1][j - 1] - prices[j])  # 保持满仓or买入
        #print(dp0,dp1)
        return dp0[-1][-1]
            
        