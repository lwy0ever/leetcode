class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp + 内存优化
        pre2 = 0
        pre1 = 0
        for i in range(2,len(cost) + 1):
            pre1,pre2 = min(pre2 + cost[i - 2],pre1 + cost[i - 1]),pre1
        return pre1

        '''
        # dp
        n = len(cost)
        dp = [0] * (n + 1)  # dp[i]表示到达i所需要的最小体力
        for i in range(2,n + 1):    # 0不需要到达
            dp[i] = min(dp[i - 1] + cost[i - 1],dp[i - 2] + cost[i - 2])
        return dp[-1]
        '''