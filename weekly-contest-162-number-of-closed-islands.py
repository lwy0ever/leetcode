class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        #for i in range(n):
        #    grid[i] = [0] + grid[i] + [0]
        #grid = [[0] * (m + 2)] + grid + [[0] * (m + 2)]
        #print(grid)
        ds = [[-1,0],[1,0],[0,-1],[0,1]]
        def dfs(x,y):
            grid[x][y] = 1
            for d in ds:
                if 0 <= x + d[0] < n and 0 <= y + d[1] < m and grid[x + d[0]][y + d[1]] == 0:
                    dfs(x + d[0],y + d[1])
        for i in range(n):
            if grid[i][0] == 0:
                dfs(i,0)
            if grid[i][m - 1] == 0:
                dfs(i,m - 1)
        for i in range(m):
            if grid[0][i] == 0:
                dfs(0,i)
            if grid[n - 1][i] == 0:
                dfs(n - 1,i)
        #print(grid)
        
        ans = 0
        for i in range(1,n - 1):
            for j in range(1,m - 1):
                if grid[i][j] == 0:
                    ans += 1
                    dfs(i,j)
        return ans
                    