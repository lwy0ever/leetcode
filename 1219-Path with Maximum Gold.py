class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)
        m = len(grid[0])
        def go(visited,i,j,gold):
            ma = gold
            di = [[0,-1],[0,1],[1,0],[-1,0]]
            for d in di:
                x = i + d[0]
                y = j + d[1]
                if x >= 0 and x < n and y >= 0 and y < m and (x,y) not in visited:
                    if grid[x][y] > 0:
                        visited.add((x,y))
                        ma = max(ma,go(visited,x,y,gold + grid[x][y]))
                        visited.remove((x,y))
            return ma

        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    visited = {(i,j)}
                    ans = max(ans,go(visited,i,j,grid[i][j]))
        return ans