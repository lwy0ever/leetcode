class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        di = [(-1,0),(1,0),(0,-1),(0,1)]
        # bfs
        fromP = [(0,0,0)]   # (i,j,l)表示到达(i,j)点,已经使用l次消除
        visited = {(0,0,0)}
        cnt = 0
        while fromP:
            toP = []
            for p in fromP:
                if p[0] == n - 1 and p[1] == m - 1:
                    return cnt
                for d in di:
                    if 0 <= p[0] + d[0] < n and 0 <= p[1] + d[1] < m:
                        if grid[p[0] + d[0]][p[1] + d[1]] == 0 and (p[0] + d[0],p[1] + d[1],p[2]) not in visited:
                            toP.append((p[0] + d[0],p[1] + d[1],p[2]))
                            visited.add((p[0] + d[0],p[1] + d[1],p[2]))
                        elif grid[p[0] + d[0]][p[1] + d[1]] == 1 and p[2] + 1 <= k and (p[0] + d[0],p[1] + d[1],p[2] + 1) not in visited:
                            toP.append((p[0] + d[0],p[1] + d[1],p[2] + 1))
                            visited.add((p[0] + d[0],p[1] + d[1],p[2] + 1))
            fromP = toP
            #print(fromP)
            cnt += 1
        return -1