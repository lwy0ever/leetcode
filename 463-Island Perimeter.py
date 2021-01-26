class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        di = [(-1,0),(1,0),(0,-1),(0,1)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                for dx,dy in di:
                    if 0 <= i + dx < m and 0 <= j + dy < n:
                        if grid[i + dx][j + dy] == 0:
                            ans += 1
                    else:
                        ans += 1
        return ans
                    