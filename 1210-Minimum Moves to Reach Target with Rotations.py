class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[n - 1][n - 2] or grid[n - 1][n - 1]:
            return -1
        #di = [[0,1,0,1],[1,0,1,0],[0,0,1,-1],[0,0,-1,1]]
        # dpH和dpV记录的是左/上点到达这个点需要的步骤
        dpH = [[float('inf')] * (n - 1) for _ in range(n)] # 成横向，记录的是左点
        dpV = [[float('inf')] * (n - 1) for _ in range(n)] # 成纵向，记录的是上点
        dpH[0][0] = 0
        for i in range(n):
            for j in range(n - 1):
                # 横向，右移
                if j - 1 >= 0 and grid[i][j - 1] == 0 and grid[i][j] == 0 and grid[i][j + 1] == 0:
                    dpH[i][j] = min(dpH[i][j],dpH[i][j - 1] + 1)
                # 纵向，右移
                if j - 1 >= 0 and i + 1 < n and grid[i][j - 1] == 0 and grid[i + 1][j - 1] == 0 and grid[i][j] == 0 and grid[i + 1][j] == 0:
                    dpV[i][j] = min(dpV[i][j],dpV[i][j - 1] + 1)
                # 横向，下移
                if i - 1 >= 0 and grid[i - 1][j] == 0 and grid[i - 1][j + 1] == 0 and grid[i][j] == 0 and grid[i][j + 1] == 0:
                    dpH[i][j] = min(dpH[i][j],dpH[i - 1][j] + 1)
                # 纵向，下移
                if i - 1 >= 0 and i + 1 < n and grid[i - 1][j] == 0 and grid[i][j] == 0 and grid[i + 1][j] == 0:
                    dpV[i][j] = min(dpV[i][j],dpV[i - 1][j] + 1)
                # 横向转成纵向/纵向转成横向
                if i + 1 < n and grid[i][j] == 0 and grid[i][j + 1] == 0 and grid[i + 1][j] == 0 and grid[i + 1][j + 1] == 0:
                    # 横向转成纵向
                    dpV[i][j] = min(dpV[i][j],dpH[i][j] + 1)
                    # 纵向转成横向
                    dpH[i][j] = min(dpH[i][j],dpV[i][j] + 1)
                #print(dpH,dpV)
        return dpH[n - 1][n - 2] if dpH[n - 1][n - 2] < float('inf') else -1
