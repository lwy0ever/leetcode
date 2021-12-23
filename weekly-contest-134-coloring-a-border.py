class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        # 边界的特点:4个方向上有不同色的色块
        # bfs
        di = ((-1,0),(1,0),(0,-1),(0,1))
        m = len(grid)
        n = len(grid[0])
        fromP = {(row,col)}
        cl = grid[row][col]  # 起点颜色
        edges = set()
        visited = set()
        while fromP:
            toP = set()
            for r,c in fromP:
                for dx,dy in di:
                    if r + dx < 0 or r + dx >= m or c + dy < 0 or c + dy >= n:  # 说明r,c在网格的边界上
                        edges.add((r,c))
                    else:
                        if grid[r + dx][c + dy] != cl:  # 说明r,c是颜色边界
                            edges.add((r,c))
                        else:
                            if (r + dx,c + dy) not in visited:
                                toP.add((r + dx,c + dy))
                                visited.add((r + dx,c + dy))
            fromP = toP
        #print(edges)
        for r,c in edges:
            grid[r][c] = color
        return grid