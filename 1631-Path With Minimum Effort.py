class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # 方法1
        # 改进方法2,每次从effort最小的点进行尝试,这样就不会出现一个点被反复尝试的情况了
        di = [(-1,0),(1,0),(0,-1),(0,1)]
        m = len(heights)
        n = len(heights[0])
        status = [(0,0,0)]   # status[i] = (e,x,y)表示到达(x,y)所需要的体力是e
        visited = set((0,0))
        while True:
            e,fx,fy = heapq.heappop(status)
            if fx == m - 1 and fy == n - 1:
                return e
            if (fx,fy) in visited:
                continue
            visited.add((fx,fy))
            for dx,dy in di:
                if 0 <= fx + dx < m and 0 <= fy + dy < n:
                    minEff = max(e,abs(heights[fx][fy] - heights[fx + dx][fy + dy]))
                    heapq.heappush(status,(minEff,fx + dx,fy + dy))
    
        # 方法2:
        # 逐个点尝试,如果该点有更小effort的方式到达,则重新尝试
        '''
        di = [(-1,0),(1,0),(0,-1),(0,1)]
        m = len(heights)
        n = len(heights[0])
        # dp[i][j]表示到达(i,j)的最小体力数
        dp = [[float('inf')] * n for _ in range(m)]
        dp[0][0] = 0
        # bfs
        fromP = {(0,0)}
        while fromP:
            toP = set()
            for fx,fy in fromP:
                for dx,dy in di:
                    if 0 <= fx + dx < m and 0 <= fy + dy < n:
                        minEff = max(dp[fx][fy],abs(heights[fx][fy] - heights[fx + dx][fy + dy]))
                        if minEff < dp[fx + dx][fy + dy]:
                            toP.add((fx + dx,fy + dy))
                            dp[fx + dx][fy + dy] = minEff
            fromP = toP
            #print(fromP)
        #print(dp)
        return dp[-1][-1]
        '''