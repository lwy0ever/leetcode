class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # 从0元素开始进行bfs
        di = [(-1,0),(1,0),(0,-1),(0,1)]
        m = len(matrix)
        n = len(matrix[0])
        ans = [[float('inf')] * n for _ in range(m)]
        fromP = list()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    fromP.append((i,j))
                    ans[i][j] = 0
        length = 0
        while fromP:
            toP = list()
            length += 1
            for fx,fy in fromP:
                for dx,dy in di:
                    if 0 <= fx + dx < m and 0 <= fy + dy < n:
                        if ans[fx + dx][fy + dy] == float('inf'):
                            ans[fx + dx][fy + dy] = length
                            toP.append((fx + dx,fy + dy))
            fromP = toP
        return ans