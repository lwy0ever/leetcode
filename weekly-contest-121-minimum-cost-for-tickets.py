class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1) # dp[i]表示第i天需要的费用,dp[0]=0,无花费
        idx = 0 # 数组days的下表
        for i in range(1,days[-1] + 1):
            if i == days[idx]:  # 这天需要旅行
                dp[i] = min(dp[max(0,i - 1)] + costs[0],
                            dp[max(0,i - 7)] + costs[1],
                            dp[max(0,i - 30)] + costs[2])
                idx += 1
            else:
                dp[i] = dp[i - 1]
        #print(dp)
        return dp[-1]