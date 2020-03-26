class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        m = collections.defaultdict(list)
        for f,to in edges:
            m[f].append(to)
            m[to].append(f)
        #print(m)
        
        visited = {1}
        fromP = {1:1}
        for i in range(t):
            toP = dict()
            for f in fromP.keys():
                cnt = 0
                dt = dict()
                for to in m[f]:
                    if to not in visited:
                        cnt += 1
                        dt[to] = 0
                        visited.add(to)
                if cnt > 0:
                    for to in dt:
                        dt[to] = fromP[f] / cnt
                    toP.update(dt)
                else:
                    toP[f] = fromP[f]
            fromP = toP
            #print(i,fromP)
        if target in fromP:
            return fromP[target]
        else:
            return 0