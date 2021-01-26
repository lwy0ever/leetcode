class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        link = collections.defaultdict(set)
        for f,t in edges:
            link[f].add(t)
            link[t].add(f)
        # 用数组建立一个树,以1为根,每个节点存放节点深度,父节点
        tree = [{'level':-1,'father':0} for i in range(n + 1)]
        tree[1]['level'] = 0
        # bfs建立树
        fromP = {1}
        l = 0
        while fromP:
            l += 1
            toP = []
            for f in fromP:
                for t in link[f]:
                    if t != tree[f]['father']:
                        tree[t]['level'] = l
                        tree[t]['father'] = f
                        toP.append(t)
            fromP = toP
        #print(tree)
        dist = dict()
        def caldist(x,y):
            if x == y:
                return 0
            if x > y:
                return caldist(y,x)
            if (x,y) in dist:
                return dist[(x,y)]
            if tree[x]['level'] < tree[y]['level']:
                dist[(x,y)] = 1 + caldist(x,tree[y]['father'])
            elif tree[x]['level'] > tree[y]['level']:
                dist[(x,y)] = 1 + caldist(tree[x]['father'],y)
            else:
                dist[(x,y)] = 2 + caldist(tree[x]['father'],tree[y]['father'])
            return dist[(x,y)]
        # 以二进制形式表示子集情况
        ans = [0] * n
        fromP = dict()
        for i in range(n):
            fromP[1 << i] = set()   # 记录城市集的邻居
            for l in link[i + 1]:
                fromP[1 << i].add(l)
        #print(fromP)
        maxDist = [0] * (1 << n)
        for _ in range(n - 1):  # 向fromP增加城市,从1个城市增加到n个城市,需要增加n - 1次
            toP = dict()
            for f in fromP.keys():
                for neighbor in fromP[f]:   # 尝试增加邻居
                    newStat = f | (1 << neighbor - 1)
                    if newStat in toP:
                        continue
                    toP[newStat] = fromP[f].copy()
                    toP[newStat].remove(neighbor)
                    for nn in link[neighbor]:
                        if 1 << (nn - 1) & newStat == 0:    # 不在城市集里面,是新邻居
                            toP[newStat].add(nn)
                    maxDist[newStat] = maxDist[f]   # 新状态的最远距离,初始化为前一个状态的最远距离
                    for x in range(n):  # 计算距离
                        if 1 << x & f:
                            maxDist[newStat] = max(maxDist[newStat],caldist(x + 1,neighbor))
                            #print(bin(f),bin(newStat),x + 1,neighbor,caldist(x + 1,neighbor))
                    #print(toP[newStat])
                    ans[maxDist[newStat]] += 1
            fromP = toP
            #print(fromP)
            #print([(bin(k),v) for k,v in fromP.items()])
            #print(maxDist)
            #print(ans,toP)
        return ans[1:]