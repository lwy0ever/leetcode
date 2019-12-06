class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon)
        m = len(dungeon[0])
        dp = [[0] * m for _ in range(n)]    # dp[i][j]表示到达(i,j)所需最少的health
        # 需要额外判断dp[i][j]是否大于0,因为小于等于0就die了

        # 从右下到左上逐步判断
        dp[n - 1][m - 1] = 1 if dungeon[n - 1][m - 1] > 0 else -dungeon[n - 1][m - 1] + 1
        #print(dp)
        for i in range(m - 2,-1,-1):
            dp[n - 1][i] = dp[n - 1][i + 1] - dungeon[n - 1][i]
            if dp[n - 1][i] <= 0:
                dp[n - 1][i] = 1
        for i in range(n - 2,-1,-1):
            dp[i][m - 1] = dp[i + 1][m - 1] - dungeon[i][m - 1]
            if dp[i][m - 1] <= 0:
                dp[i][m - 1] = 1
        
        for i in range(n - 2,-1,-1):
            for j in range(m - 2,-1,-1):
                dp[i][j] = min(dp[i][j + 1],dp[i + 1][j]) - dungeon[i][j]
                if dp[i][j] <= 0:
                    dp[i][j] = 1
        #print(dp)
        return dp[0][0]