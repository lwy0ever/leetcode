class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # m房子数
        # n颜色号,1-n
        # target目标街区数,1-target
        # dp[i][j][b]表示第i个房子刷颜色j,结果组成b个街区时的最少花费金额
        dp = [[[float('inf')] * target for _ in range(n)] for _ in range(m)]
        for i in range(m):  # 当前房子编号
            painted = False # 决定是否有花费
            colors = [] # 房子i可以涂的颜色列表
            if houses[i] == 0:  # 可以涂色
                colors = [c for c in range(n)]
            else:   # 不可以涂色
                colors = [houses[i] - 1]
                painted = True
            for c in colors:
                if i == 0:
                    if painted:
                        dp[i][c][0] = 0
                    else:
                        dp[i][c][0] = cost[i][c]
                else:
                    for preColor in range(n):   # 前一个房子的颜色
                        for block in range(target): # 当前的街区数
                            if c == preColor:
                                if painted:
                                    dp[i][c][block] = min(dp[i][c][block],dp[i - 1][c][block])
                                else:
                                    dp[i][c][block] = min(dp[i][c][block],dp[i - 1][c][block] + cost[i][c])
                            else:
                                if block == 0:  # 已经有target个街区,不再考虑
                                    continue
                                if painted:
                                    dp[i][c][block] = min(dp[i][c][block],dp[i - 1][preColor][block - 1])
                                else:
                                    dp[i][c][block] = min(dp[i][c][block],dp[i - 1][preColor][block - 1] + cost[i][c])
                    #print(dp)
        ans = float('inf')
        for c in range(n):
            ans = min(ans,dp[m - 1][c][target - 1])
        return ans if ans < float('inf') else -1