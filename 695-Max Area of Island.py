class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(g,i,j,r,c,direct):
            res = 0
            for da,db in direct:
                if i + da >= 0 and i + da < r and j + db >= 0 and j + db < c:
                    if grid[i + da][j + db] == 1:
                        grid[i + da][j + db] = 0
                        res += 1 + dfs(g,i + da,j + db,r,c,direct)
            return res
                                

        ans = 0
        r = len(grid)
        c = len(grid[0])
        direct = [(-1,0),(1,0),(0,-1),(0,1)]
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    ans = max(ans, 1 + dfs(grid,i,j,r,c,direct))
        return ans
        '''
        def bfs(g,i,j,r,c,direct):
            cnt = 1
            area = [(i,j)]
            grid[i][j] = 0
            while area:
                newArea = []
                for i,j in area:
                    for da,db in direct:
                        if i + da >= 0 and i + da < r and j + db >= 0 and j + db < c:
                            if grid[i + da][j + db] == 1:
                                cnt += 1
                                newArea.append((i + da,j + db))
                                grid[i + da][j + db] = 0
                area = newArea
            return cnt
                                

        ans = 0
        r = len(grid)
        c = len(grid[0])
        direct = [(-1,0),(1,0),(0,-1),(0,1)]
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    ans = max(ans,bfs(grid,i,j,r,c,direct))
        return ans
        '''