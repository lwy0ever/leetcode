class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # bfs
        # 从找到的第一个1开始bfs,确定第一个岛的边界(边界条件:上下左右至少有1个0),并且把点都设置为2
        # 从边界开始bfs,计算找到1的步数
        n = len(grid)   # A.length == A[0].length
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 2
                    break
            else:
                continue
            break
        #print(i,j)
        di = [[-1,0],[1,0],[0,-1],[0,1]]
        fromP = [[i,j]]
        edge = []
        while fromP:
            px,py = fromP.pop()
            isEdge = False
            for dx,dy in di:
                if 0 <= px + dx < n and 0 <= py + dy < n:
                    if grid[px + dx][py + dy] == 1:
                        fromP.append([px + dx,py + dy])
                        grid[px + dx][py + dy] = 2
                    elif grid[px + dx][py + dy] == 0:
                        isEdge = True
            if isEdge:
                edge.append([px,py])
        #print(edge)
        #print(grid)
        ans = 0
        while True:
            #print(edge)
            newEdge = set()
            for px,py in edge:
                for dx,dy in di:
                    if 0 <= px + dx < n and 0 <= py + dy < n:
                        if grid[px + dx][py + dy] == 0:
                            newEdge.add((px + dx,py + dy))
                            grid[px + dx][py + dy] = 2
                        elif grid[px + dx][py + dy] == 1:
                            return ans
            edge = newEdge
            ans += 1