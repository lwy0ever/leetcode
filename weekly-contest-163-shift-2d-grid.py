class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        r = (k // n) % m
        c = k % n
        #print(r,c)
        if r > 0:
            grid = grid[-r:] + grid[:-r]
        #print(grid)
        if c > 0:
            last = grid[-1][-c:]
            for i in range(m):
                grid[i],last = last + grid[i][:-c],grid[i][-c:]
                #print(grid[i],last)
        return grid