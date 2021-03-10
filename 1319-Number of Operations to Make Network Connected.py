class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        cnum = len(connections)
        if cnum + 1 < n:
            return -1
        d = collections.defaultdict(set)
        for a,b in connections:
            d[a].add(b)
            d[b].add(a)
        #print(d)
        toCon = set([i for i in range(n)])
        ans = -1
        while toCon:
            p = toCon.pop()
            #print(p,toCon)
            # bfs
            fromP = set()
            fromP.add(p)            
            while fromP:
                toP = set()
                for f in fromP:
                    for t in d[f]:
                        if t in toCon:
                            toP.add(t)
                            toCon.remove(t)
                fromP = toP
            ans += 1
        return ans