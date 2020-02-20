class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    ans += n - j
                    break
        return ans