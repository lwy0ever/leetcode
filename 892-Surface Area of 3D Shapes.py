class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        # 从6个方向去看
        n = len(grid)
        m = len(grid[0])
        ans = 0
        # 俯瞰
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    ans += 2
        # 从左右看
        for i in range(n):
            pre = 0
            for j in range(m):
                ans += abs(grid[i][j] - pre)
                pre = grid[i][j]
            ans += (pre - 0)
        # 从上下看
        for i in range(m):
            pre = 0
            for j in range(n):
                ans += abs(grid[j][i] - pre)
                pre = grid[j][i]
            ans += (pre - 0)
        return ans