class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        # 假定当前单元格是1,也就是\
        # 这时候需要检查右侧的单元格
        # 1:\,球移动到右下
        # 2:/,卡死
        # 3:|(边界),卡死
        # 当前单元格是/时类似

        # 简化:
        # 当前单元格是grid[i][j],定义grid[i][j]的值是direction
        # 需要考察grid[i][j + direction],如果没有超出边界,并且和grid[i][j]通向
        # 则小球下移到下一行的j + direction列
        m = len(grid)
        n = len(grid[0])
        ans = [-1] * n
        for i in range(n):
            col = i
            for j in range(m):
                if 0 <= col + grid[j][col] < n and grid[j][col + grid[j][col]] == grid[j][col]:
                    col += grid[j][col]
                else:
                    break
            else:
                ans[i] = col
        return ans