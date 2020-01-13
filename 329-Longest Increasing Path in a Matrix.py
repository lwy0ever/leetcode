class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # dfs,通过将数据存储在maxPath,有效避免重复计算
        di = [(-1,0),(1,0),(0,-1),(0,1)]
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        maxPath = [[0] * m for _ in range(n)]   # maxPath记录从当前点出发的最长路径
        
        def dfs(i,j):
            if maxPath[i][j] != 0:
                return maxPath[i][j]
            ans = 1
            for d in di:
                x = i + d[0]
                y = j + d[1]
                if 0 <= x < n and 0 <= y < m:
                    if matrix[i][j] < matrix[x][y]:
                        ans = max(ans,dfs(x,y) + 1)
            maxPath[i][j] = ans
            return ans
        
        ans = 1
        for i in range(n):
            for j in range(m):
                ans = max(ans,dfs(i,j))
        return ans

        '''
        di = [(-1,0),(1,0),(0,-1),(0,1)]
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        # 先找到所有的坑(该点小于等于其周围的所有点)
        holes = []
        for i in range(n):
            for j in range(m):
                for d in di:
                    x = i + d[0]
                    y = j + d[1]
                    if 0 <= x < n and 0 <= y < m:
                        if matrix[i][j] > matrix[x][y]:
                            break
                else:
                    holes.append((i,j))
        #print(holes)
        #maxPath = [[1] * m for _ in range(n)]   # maxPath记录到达当前点的最长路径
        ans = 1
        # 类似bfs
        # bfs会造成重复计算的问题,速度慢
        path = 0
        fromP = set(holes)
        while fromP:
            path += 1
            toP = set()
            for i,j in fromP:
                for d in di:
                    x = i + d[0]
                    y = j + d[1]
                    if 0 <= x < n and 0 <= y < m:
                        if matrix[i][j] < matrix[x][y]:
                            toP.add((x,y))
                            #if maxPath[x][y] < path + 1:
                            #maxPath[x][y] = path + 1
            print(fromP,toP,maxPath)
            fromP = toP
        ans = path
        return ans
        '''