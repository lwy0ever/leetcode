class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directs = [(-1,-2),(-1,2),(-2,-1),(-2,1),(1,2),(1,-2),(2,1),(2,-1)]
        ma = 310
        x = abs(x)
        y = abs(y)
        area = [[999] * ma for _ in range(ma)]    #棋盘，默认需要999步能够到达
        startx = 5
        starty = 5
        x += 5
        y += 5
        #print(x,y)
        stack = {(startx,starty)}
        area[startx][starty] = 0
        while stack:
            nstack = set()
            for nx,ny in stack:
                step = area[nx][ny]
                for dx,dy in directs:
                    if nx + dx >= 0 and nx + dx < ma and ny + dy >= 0 and ny + dy < ma:
                        if area[nx + dx][ny + dy] > step + 1:
                            area[nx + dx][ny + dy] = step + 1
                            nstack.add((nx + dx,ny + dy))
                            if nx + dx == x and ny + dy == y:
                                return step + 1
            stack = nstack
            #print(stack)
            #for i in range(ma):
            #    print(area[i])
        return area[x][y]
                    
        