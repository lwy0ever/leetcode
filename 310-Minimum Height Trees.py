class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        es = collections.defaultdict(set)
        for a,b in edges:
            es[a].add(b)
            es[b].add(a)
        #print(es)
        
        if n <= 2:
            return [i for i in range(n)]
        
        # 每次将链接数为1的节点删除,直到剩余1or2个节点
        point = {k for k in es if len(es[k]) == 1} # 结点数为1的结点
        while n > 2:
            newPoint = set()
            for p in point:
                linked = es[p].pop()
                del es[p]
                es[linked].remove(p)
                if len(es[linked]) == 1:
                    newPoint.add(linked)
                n -= 1
            point = newPoint
            #print(points)
        return list(point)