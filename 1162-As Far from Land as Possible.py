class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        # 从所有的1开始，bfs找到最远的0
        #visited = set()
        fromP = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fromP.add((i,j))
                    #visited.add((i,j))
        ans = -1
        di = [(-1,0),(1,0),(0,-1),(0,1)]
        # bfs
        while fromP:
            toP = set()
            for fx,fy in fromP:
                for dx,dy in di:
                    if 0 <= fx + dx < n and 0 <= fy + dy < m:
                        if grid[fx + dx][fy + dy] == 0:
                            toP.add((fx + dx,fy + dy))
                            grid[fx + dx][fy + dy] = 1
                            #visited.add((fx + dx,fy + dy))
            fromP = toP
            ans += 1
        return ans if ans > 0 else -1