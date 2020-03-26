class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # 我们将最外围的一圈看成是围墙，向里面更新围墙的高度
        # 由于雨水会从最低的位置流出，因此我们从围墙最低的位置开始，判断墙内的是能否积水，如果能够积水，表示墙内的节点高度较小，这时候能够累计差值的水，并更新这个点的墙的高度
        # 不断从最低处向内更新墙的高度，直到所有节点都被访问为止
        import heapq
        if not heightMap:
            return 0
        n = len(heightMap)
        m = len(heightMap[0])
        ans = 0
        heap = []   # heap[i][0]存储高度,heap[i][1]和heap[i][2]存储坐标
        visited = [[0] * m for _ in range(n)]
        di = [(0,1),(0,-1),(1,0),(-1,0)]
        
        for i in range(n):
            heapq.heappush(heap,[heightMap[i][0],i,0])
            visited[i][0] = 1
            heapq.heappush(heap,[heightMap[i][m - 1],i,m - 1])
            visited[i][m - 1] = 1
        
        for i in range(m):
            heapq.heappush(heap,[heightMap[0][i],0,i])
            visited[0][i] = 1
            heapq.heappush(heap,[heightMap[n - 1][i],n - 1,i])
            visited[n - 1][i] = 1
        
        while heap:
            height,r,c = heapq.heappop(heap)
            for dr,dc in di:
                nr,nc = r + dr,c + dc
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                    maxHeight = max(height,heightMap[nr][nc])
                    ans += maxHeight - heightMap[nr][nc]
                    heapq.heappush(heap,[maxHeight,nr,nc])
                    visited[nr][nc] = 1
        return ans