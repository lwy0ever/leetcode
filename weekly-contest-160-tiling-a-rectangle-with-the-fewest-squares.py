class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        # dp[i][j]表示铺满i * j的单元格需要的瓷砖数
        dp = [[n * m] * (m + 1) for _ in range(n + 1)]
        for i in range(1,n + 1):
            for j in range(1,m + 1):
                if i == j:
                    dp[i][j] = 1
                # 方案1:将i分成p和i - p两部分
                for p in range(1,i):
                    dp[i][j] = min(dp[i][j],dp[p][j] + dp[i - p][j])
                # 方案2:将j分成p和j - p两部分
                for p in range(1,j):
                    dp[i][j] = min(dp[i][j],dp[i][p] + dp[i][j - p])
                # 方案3:分成4 + 1块,中间一块的大小是1x1,坐标是(x-1,y-1)到(x,y)
                for x in range(2,i):
                    for y in range(2,j):
                        dp[i][j] = min(dp[i][j],dp[x - 1][y] + dp[x][j - y] + dp[i - x + 1][y - 1] + dp[i - x][j - y + 1] + 1)
        return dp[n][m]