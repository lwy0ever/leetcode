class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dpE = [0] * n   # 表示第i天空仓情况下的最大收益
        dpF = [0] * n   # 表示第i天满仓情况下的最大收益
        dpF[0] = -prices[0]
        for i in range(1,n):
            dpE[i] = max(dpE[i - 1],dpF[i - 1] + prices[i]) #保持空仓or卖出
            dpF[i] = max(dpF[i - 1],dpE[i - 2] - prices[i]) #保持满仓or买入,由于cooldown的存在,买入时只能使用dpE[i - 2],不能用dpE[i - 1]
        return dpE[-1]