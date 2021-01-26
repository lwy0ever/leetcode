class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # 并查集 + dfs
        # 非优化状态,每个stones之间都需要记录连接状态
        # 优化后,相同行/列只需要记录一个连接状态
        n = len(stones)
        dictX = collections.defaultdict(list)
        dictY = collections.defaultdict(list)
        for i,(x,y) in enumerate(stones):
            dictX[x].append(i)
            dictY[y].append(i)
        visited = set()
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for i in dictX[stones[node][0]]:
                dfs(i)
            for i in dictY[stones[node][1]]:
                dfs(i)
                
        ans = 0
        for i in range(n):
            if i not in visited:
                ans += 1
                dfs(i)
        return n - ans
        
        '''
        # 并查集 + dfs
        n = len(stones)
        link = collections.defaultdict(list)    # link[i]存储和stones[i]直接连接的stones的坐标
        for i,(x1,y1) in enumerate(stones):
            for j,(x2,y2) in enumerate(stones):
                if i != j and (x1 == x2 or y1 == y2):
                    link[i].append(j)
        visited = set()
        
        def dfs(p):  # 连接当前点的所有点
            visited.add(p)
            for t in link[p]:
                if t not in visited:
                    dfs(t)
        
        ans = 0
        for i in range(n):
            if i not in visited:
                ans += 1
                dfs(i)
        return n - ans
        '''