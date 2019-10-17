class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        ans = 1
        cellFrom = {(0,0)}
        grid[0][0] = 1
        di = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        while cellFrom:
            if (n - 1,n - 1) in cellFrom:
                return ans
            cellTo = set()
            for fx,fy in cellFrom:
                for dx,dy in di:
                    if fx + dx >= 0 and fx + dx < n and fy + dy >= 0 and fy + dy < n and grid[fx + dx][fy + dy] == 0:
                        cellTo.add((fx + dx,fy + dy))
                        grid[fx + dx][fy + dy] = 1
            ans += 1
            cellFrom = cellTo
        return -1