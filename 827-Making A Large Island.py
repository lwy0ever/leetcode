class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # area[i][j][0]记录包含grid[i][j]的岛屿的面积
        # area[i][j][0]记录包含grid[i][j]的岛屿的编号,从1开始
        area = [[[0,0] for _ in range(n)] for _ in range(m)]
        
        di = [[-1,0],[1,0],[0,-1],[0,1]]
        counter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                if area[i][j][1] > 0:  # 之前记录过
                    continue
                counter += 1
                visited = {(i,j)}
                fromP = {(i,j)}
                cnt = 1
                while fromP:
                    toP = set()
                    for fx,fy in fromP:
                        for dx,dy in di:
                            if 0 <= fx + dx < m and 0 <= fy + dy < n:
                                if grid[fx + dx][fy + dy] == 1 and (fx + dx,fy + dy) not in visited:
                                    visited.add((fx + dx,fy + dy))
                                    toP.add((fx + dx,fy + dy))
                                    cnt += 1
                    fromP = toP
                for x,y in visited:
                    area[x][y] = (cnt,counter)
        #print(area)
        ans = 1
        for i in range(m):
            for j in range(n):
                ans = max(ans,area[i][j][0])
                if grid[i][j] == 1:
                    continue
                t = 1
                used = set()
                for dx,dy in di:
                    if 0 <= i + dx < m and 0 <= j + dy < n:
                        if area[i + dx][j + dy][1] not in used:
                            t += area[i + dx][j + dy][0]
                            used.add(area[i + dx][j + dy][1])
                ans = max(ans,t)
        return ans
