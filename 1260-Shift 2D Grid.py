class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        ans = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                ori = i * m + j - k
                while ori < 0:
                    ori += m * n
                ans[i][j] = grid[ori // m][ori % m]
        #print(ans)
        return ans