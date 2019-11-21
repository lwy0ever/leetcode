class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        di = [(-1,0),(0,-1),(1,0),(0,1)]
        
        # 计算在box和keeper两个位置的情况下，keeper可以到达的位置
        def bfs(box,keeper):
            #print(box,keeper)
            fromP = {keeper}
            visited = {keeper}
            while fromP:
                #print(fromP)
                #print(visited)
                toP = set()
                for f in fromP:
                    for d in di:
                        t = (f[0] + d[0],f[1] + d[1])
                        if 0 <= t[0] < n and 0 <= t[1] < m:
                            if grid[t[0]][t[1]] != '#' and t != box:
                                if t not in visited:
                                    visited.add(t)
                                    toP.add(t)
                #print(toP)
                fromP = toP
            return visited
        
        # 初始化3个位置
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'T':
                    target = (i,j)
                elif grid[i][j] == 'S':
                    start = (i,j)
                elif grid[i][j] == 'B':
                    box = (i,j)
        
        ans = 1
        fromStatus = set()  # box,keeper
        visitedStatus = set()   # box,keeper
        # 初始化keeper到可以推箱子的位置
        keeperCanReach = bfs(box,start)
        #print(keeperCanReach)
        for d in di:
            if (box[0] + d[0],box[1] + d[1]) in keeperCanReach: # keeper到达的位置
                fromStatus.add((box,(box[0] + d[0],box[1] + d[1])))
                visitedStatus.add((box,(box[0] + d[0],box[1] + d[1])))
        while fromStatus:
            #print(fromStatus)
            #print(visitedStatus)
            toStatus = set()
            for f in fromStatus:
                tocheck = []
                for d in di[:2]:
                    a = (f[0][0] + d[0],f[0][1] + d[1])
                    b = (f[0][0] - d[0],f[0][1] - d[1])
                    if 0 <= a[0] < n and 0 <= a[1] < m and 0 <= b[0] < n and 0 <= b[1] < m and grid[a[0]][a[1]] != '#' and grid[b[0]][b[1]] != '#':
                        tocheck.append((a,b))
                        tocheck.append((b,a))
                if not tocheck:
                    continue
                keeperCanReach = bfs(f[0],f[1])
                for a,b in tocheck:
                    if a in keeperCanReach: # keeper到达的位置
                        if (b,f[0]) not in visitedStatus:
                                if b == target:
                                    return ans
                                visitedStatus.add((b,f[0]))
                                toStatus.add((b,f[0]))    # box位置就是keeper的新位置
            fromStatus = toStatus
            ans += 1
        return -1
