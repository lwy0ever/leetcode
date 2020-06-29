class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        # 如果要获得最短距离,应该选择 中位数
        # 以dis[i][j]表示在houses[i:j + 1]的范围内,放置1个邮筒,最短的距离
        n = len(houses)
        houses.sort()
        dis = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1,n):
                mid = (i + j) // 2
                m = (i + j) / 2
                for t in range(i,int(m + 1)):
                    #print(i,j,t,m,m + m -t)
                    dis[i][j] += (houses[int(m + (m - t))] - houses[t])
                #print(i,j,dis[i][j])
        # 以dp[i][j]表示在houses[:i + 1]放置j + 1个邮筒的最短距离
        # dp[i][j] = min(dp[t - 1][j - 1] + dis[t][i],dp[i][j])
        dp = [[float('inf')] * k for _ in range(n)]
        for i in range(n):
            dp[i][0] = dis[0][i]    # 处理1个邮筒的情况
            for j in range(1,min(i + 1,k)): # 从2个邮筒开始考虑;i + 1个house,最多i + 1个邮筒(下标为i) or k个邮筒
                for t in range(j,i + 1):    # 将i + 1个house分成1到j和j + 1到i + 1两部分
                    dp[i][j] = min(dp[i][j],dp[t - 1][j - 1] + dis[t][i])
                    #print(i,j,t,dp[t - 1][j - 1] + dis[t][i])
        return dp[n - 1][k - 1]