class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        if grid[0][0] == 0:
            return 0
        dpMin = [1] * n    # 最小值
        dpMax = [-1] * n   # 最大值
        dpMin[0] = grid[0][0]
        dpMax[0] = grid[0][0]
        for i in range(1,n):
            m = dpMin[i - 1] * grid[0][i]
            dpMin[i],dpMax[i] = m,m
        #print(dpMin)
        #print(dpMax)
        for r in grid[1:]:
            m = dpMin[0] * r[0]
            dpMin[0],dpMax[0] = m,m
            for i in range(1,n):
                m1 = dpMin[i - 1] * r[i]
                m2 = dpMin[i] * r[i]
                m3 = dpMax[i - 1] * r[i]
                m4 = dpMax[i] * r[i]
                dpMin[i],dpMax[i] = min(m1,m2,m3,m4),max(m1,m2,m3,m4)
            #print(dpMin)
            #print(dpMax)
        return dpMax[-1] % (10 ** 9 + 7) if dpMax[-1] >= 0 else -1