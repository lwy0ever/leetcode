class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        # 从[a,b]开始bfs,如果能通过不同的路径到达[c,d],则说明存在环
        # 由于是不同路径,也就是环的长度大于等于1 + 2 + 1=4
        # 由于不能斜向走,所以到达[c,d]的时候,所需步数是一样的
        m = len(grid)
        n = len(grid[0])
        di = [[-1,0],[1,0],[0,-1],[0,1]]
        visited = set()
        for i in range(m):
            for j in range(n):
                if (i,j) in visited:
                    continue
                a = grid[i][j]
                #print(i,j)
                fromP = {(i,j)}
                visited.add((i,j))
                while fromP:
                    toP = set()
                    for f in fromP:
                        for d in di:
                            if 0 <= f[0] + d[0] < m and 0 <= f[1] + d[1] < n and grid[f[0] + d[0]][f[1] + d[1]] == a:
                                if (f[0] + d[0],f[1] + d[1]) in toP:
                                    return True
                                if (f[0] + d[0],f[1] + d[1]) not in visited:
                                    toP.add((f[0] + d[0],f[1] + d[1]))
                                    visited.add((f[0] + d[0],f[1] + d[1]))
                    fromP = toP
                    #print(fromP)
        return False