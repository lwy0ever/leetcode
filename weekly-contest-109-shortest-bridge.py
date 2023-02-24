class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # bfs
        direct = [(-1,0),(1,0),(0,-1),(0,1)]
        # 先找到一个岛上面的一个点
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    start = [i,j]
                    break
            else:
                continue
            break
        # bfs找到这个岛的全部点
        island = set([tuple(start)])
        fromP = [start]
        visited = set([tuple(start)])
        while fromP:
            newFrom = list()
            for f in fromP:
                for d in direct:
                    nx,ny = f[0] + d[0],f[1] + d[1]
                    if 0 <= nx < n and 0 <= ny < n and (nx,ny) not in visited and grid[nx][ny] == 1:
                        newFrom.append((nx,ny))
                        island.add((nx,ny))
                        visited.add((nx,ny))
            fromP = newFrom
        #print(island)
        # bfs找0,计步数
        ans = 0
        fromP = island
        visited = set(island)
        while fromP:
            newFrom = list()
            for f in fromP:
                for d in direct:
                    nx,ny = f[0] + d[0],f[1] + d[1]
                    if 0 <= nx < n and 0 <= ny < n and (nx,ny) not in visited:
                        if grid[nx][ny] == 0:
                            newFrom.append((nx,ny))
                            visited.add((nx,ny))
                        else:
                            return ans
            fromP = newFrom
            ans += 1
        return ans