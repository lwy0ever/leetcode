class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        di = [(-1,0),(1,0),(0,-1),(0,1)]
        visited = [[False] * m for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if visited[i][j]:
                    continue
                visited[i][j] = True
                if grid[i][j] == '0':
                    continue
                fromP = [(i,j)]
                ans += 1
                # bfs
                while fromP:
                    toP = []
                    for f in fromP:
                        for d in di:
                            if 0 <= f[0] + d[0] < n and 0 <= f[1] + d[1] < m:
                                if not visited[f[0] + d[0]][f[1] + d[1]] and grid[f[0] + d[0]][f[1] + d[1]] == '1':
                                    visited[f[0] + d[0]][f[1] + d[1]] = True
                                    toP.append((f[0] + d[0],f[1] + d[1]))
                    fromP = toP
        return ans