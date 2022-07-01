class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if forest[0][0] == 0:
            return -1
        
        m = len(forest)
        n = len(forest[0])
        di = [(-1,0),(1,0),(0,-1),(0,1)]

        # bfs
        def bfs(fromP,toP):
            if fromP == toP:
                return 0
            visited = {fromP}
            fs = {fromP}
            step = 0
            while fs:
                step += 1
                new_toP = set()
                for f in fs:
                    for d in di:
                        #print(f[0],d[0],f[1],d[1])
                        if 0 <= f[0] + d[0] < m and 0 <= f[1] + d[1] < n:
                            if (f[0] + d[0],f[1] + d[1]) not in visited and forest[f[0] + d[0]][f[1] + d[1]] > 0:
                                new_toP.add((f[0] + d[0],f[1] + d[1]))
                                visited.add((f[0] + d[0],f[1] + d[1]))
                if toP in new_toP:
                    return step
                fs = new_toP
            return -1                

        points = list()
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    points.append((i,j))
        points.sort(key = lambda x:forest[x[0]][x[1]])
        ans = 0
        fromP = (0,0)
        for toP in points:
            step = bfs(fromP,toP)
            if step == -1:
                return -1
            ans += step
            fromP = toP
        return ans