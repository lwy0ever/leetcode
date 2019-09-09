class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        land = []
        dis = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    land.append((i,j))
        if not land or len(land) == n * n:
            return -1
        direct = [(-1,0),(1,0),(0,1),(0,-1)]
        dis = -1
        while land:
            newLand = []
            for l in land:
                for d in direct:
                    p = (l[0] + d[0],l[1] + d[1])
                    if p[0] >= 0 and p[0] < n and p[1] >=0 and p[1] < n:
                        if grid[p[0]][p[1]] == 0:
                            newLand.append(p)
                            grid[p[0]][p[1]] = 1
            land = newLand
            dis += 1
        return dis
