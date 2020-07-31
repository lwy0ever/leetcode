class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        # 先判断是否能够到达终点
        ans = []
        if obstacleGrid[0][0] == 1: # 起点不可达
            return ans
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])
        # dp[i][j]表示(i,j)是否可以到达
        # dp[0][0]可达,则第一行\列都可达
        dp = [[0] * c for _ in range(r)]
        dp[0][0] = 1
        for i in range(1,c):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = dp[0][i - 1]
        for i in range(1,r):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i - 1][0]
        for i in range(1,r):
            for j in range(1,c):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = (dp[i - 1][j] or dp[i][j - 1])
        #print(dp)
        # 终点不可达
        if dp[-1][-1] == 0:
            return ans
        # 终点可达
        # 从终点逆向回到起点
        i = r - 1
        j = c - 1
        ans.append((i,j))
        while i > 0 or j > 0:
            if i > 0 and dp[i - 1][j]:
                i -= 1
                ans.append((i,j))
                continue
            if j > 0 and dp[i][j - 1]:
                j -= 1
                ans.append((i,j))
        return ans[::-1]
