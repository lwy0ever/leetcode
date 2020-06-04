class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        # dp[r][c1][c2]表示robot1在(r,c1),robot2在(r,c2)时,可以获得的最多数量
        dp = [[[-1] * cols for _ in range(cols)] for _ in range(rows + 1)]
        for i in range(cols):
            for j in range(cols):
                dp[rows][i][j] = 0
        def dfs(r,c1,c2):
            if dp[r][c1][c2] >= 0:
                return dp[r][c1][c2]
            row = grid[r][c1] + grid[r][c2]
            if c1 == c2:
                row -= grid[r][c2]
            nextRow = 0
            for nc1 in range(max(c1 - 1,0),min(c1 + 2,cols)):
                for nc2 in range(max(c2 - 1,0),min(c2 + 2,cols)):
                    dfs(r + 1,nc1,nc2)
                    nextRow = max(nextRow,dp[r + 1][nc1][nc2])
            dp[r][c1][c2] = row + nextRow
        dfs(0,0,cols - 1)
        return dp[0][0][cols - 1]
        