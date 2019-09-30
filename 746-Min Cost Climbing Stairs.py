class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0,0]    # dp[i]表示到i步所需的cost
        for i in range(2,n + 1):
            dp.append(min(dp[-2] + cost[i - 2],dp[-1] + cost[i - 1]))
        return dp[-1]