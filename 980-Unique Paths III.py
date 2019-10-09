class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ans = 0
        di = [(0,1),(1,0),(0,-1),(-1,0)]
        n = len(grid)
        m = len(grid[0])
        zeros = 0
        startx = 0
        starty = 0
        endx = 0
        endy = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    zeros += 1
                elif grid[i][j] == 1:
                    startx = i + 1
                    starty = j + 1
                elif grid[i][j] == 2:
                    endx = i + 1
                    endy = j + 1
            grid[i].insert(0,-1)
            grid[i].append(-1)
        grid.insert(0,[-1] * (m + 2))
        grid.append([-1] * (m + 2))
        visited = set()

        def dfs(x,y):
            for d in di:
                #print(x,y,d[0],d[1])
                if grid[x + d[0]][y + d[1]] == 2:
                    if len(visited) == zeros:
                        nonlocal ans
                        ans += 1
                elif grid[x + d[0]][y + d[1]] == 0:
                    if (x + d[0],y + d[1]) not in visited:
                        visited.add((x + d[0],y + d[1]))
                        dfs(x + d[0],y + d[1])
                        visited.remove((x + d[0],y + d[1]))
        
        #print(grid)
        #print(startx,starty)
        dfs(startx,starty)
        return ans