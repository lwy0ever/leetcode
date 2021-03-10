class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        # 每个点(x,y)分成4部分:
        # 1,上
        # 2,下
        # 3,左
        # 4,右
        # dfs
        m = len(grid)
        n = len(grid[0])
        ans = 0
        visited = set() # 记录每个x,y的每个part是否被访问过
        
        def dfs(x,y,part):
            if (x,y,part) not in visited:
                visited.add((x,y,part))
            else:
                return
            if grid[x][y] == ' ':
                for p in range(1,5):
                    if p != part:
                        dfs(x,y,p)
            elif grid[x][y] == '/':
                if part == 1:
                    dfs(x,y,3)
                if part == 2:
                    dfs(x,y,4)
                if part == 3:
                    dfs(x,y,1)
                if part == 4:
                    dfs(x,y,2)
            else:   # grid[x][y] == '\\':
                if part == 1:
                    dfs(x,y,4)
                if part == 2:
                    dfs(x,y,3)
                if part == 3:
                    dfs(x,y,2)
                if part == 4:
                    dfs(x,y,1)
            if part == 1:
                if 0 <= x - 1:
                    dfs(x - 1,y,2)
            if part == 2:
                if x + 1 < m:
                    dfs(x + 1,y,1)
            if part == 3:
                if 0 <= y - 1:
                    dfs(x,y - 1,4)
            if part == 4:
                if y + 1 < n:
                    dfs(x,y + 1,3)

        for i in range(m):
            for j in range(n):
                for p in range(1,5):
                    if (i,j,p) not in visited:
                        ans += 1
                        dfs(i,j,p)
        return ans