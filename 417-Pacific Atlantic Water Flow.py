class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        di = [(-1,0),(1,0),(0,1),(0,-1)]
        if not matrix:
            return []
        n = len(matrix)
        m = len(matrix[0])
        # 2次bfs
        # 从岸边向中间找大于等于当前点的点
        def bfs(fromP):
            ans = set()
            for p in fromP:
                ans.add(p)
            while fromP:
                toP = set()
                for fx,fy in fromP:
                    for dx,dy in di:
                        if 0 <= fx + dx < n and 0 <= fy + dy < m:
                            if matrix[fx + dx][fy + dy] >= matrix[fx][fy] and (fx + dx,fy + dy) not in ans:
                                ans.add((fx + dx,fy + dy))
                                toP.add((fx + dx,fy + dy))
                fromP = toP
            return ans
        
        fromPacific = set()
        for i in range(n):
            fromPacific.add((i,0))
        for i in range(1,m):
            fromPacific.add((0,i))
        canToPacific = bfs(fromPacific)

        fromAtlantic = set()
        for i in range(n):
            fromAtlantic.add((i,m - 1))
        for i in range(m - 1):
            fromAtlantic.add((n - 1,i))
        canToAtlantic = bfs(fromAtlantic)
        
        ans = canToPacific.intersection(canToAtlantic)
        return list(ans)