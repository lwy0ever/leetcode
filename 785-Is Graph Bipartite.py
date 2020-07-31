class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # 两个算法的思路一致:
        # 先将一个点归属图A
        # 则其相邻点归属图B
        # 相邻点的相邻点归属图A
        # 如果发现要归类的点已经有归属图,并且是正确的,则忽略
        # 如果发现要归类的点已经有归属图,并且是错误的,则返回False
        # 算法1:用数组记录归属情况
        n = len(graph)
        status = [-1] * n    # status[i]表示节点i的归属情况,-1:待定,0:图A,1:图B
        for i in range(n):
            if status[i] >= 0:
                continue
            # bfs
            fromP = {i}
            g = 0
            status[i] = g
            while fromP:
                g ^= 1
                toP = set()
                for f in fromP:
                    for t in graph[f]:
                        if status[t] < 0:
                            status[t] = g
                            toP.add(t)
                        elif status[t] != g:
                            return False
                fromP = toP
        return True

        # 算法2:用set记录归属情况
        '''
        fromP = set()
        AB = [set(),set()]
        toCheck = set(range(len(graph)))
        while toCheck:
            p = toCheck.pop()
            # bfs
            fromP.add(p)
            targetIndex = 1
            AB[targetIndex ^ 1].add(p)
            while fromP:
                toP = set()
                for p in fromP:
                    for t in graph[p]:
                        if t in AB[targetIndex ^ 1]:
                            return False
                        if t not in AB[targetIndex]:
                            toP.add(t)
                            AB[targetIndex].add(t)
                            toCheck.discard(t)
                fromP = toP
                targetIndex ^= 1
                #print(AB)
                #print(fromP)
        return True
        '''