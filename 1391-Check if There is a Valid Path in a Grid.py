class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # bfs
        n = len(grid)
        m = len(grid[0])
        up = (-1,0)
        down = (1,0)
        left = (0,-1)
        right = (0,1)
        d = {
            1:{left,right},
            2:{up,down},
            3:{left,down},
            4:{right,down},
            5:{left,up},
            6:{right,up}
        }
        fromP = {(0,0)}
        visited = {(0,0)}
        while fromP:
            if (n - 1,m - 1) in fromP:
                return True
            toP = set()
            for fx,fy in fromP:
                for dx,dy in d[grid[fx][fy]]:
                    if (fx + dx,fy + dy) in visited:
                        continue
                    if 0 <= fx + dx < n and 0 <= fy + dy < m:   # 从from点指向了一个合法的点
                        if (-dx,-dy) in d[grid[fx + dx][fy + dy]]:  # 从to点可以到达from
                            toP.add((fx + dx,fy + dy))
                            visited.add((fx + dx,fy + dy))
            fromP = toP
            #print(fromP)
        return False