class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0
        allCrossed = (1 << n) - 1
        ans = float('inf')

        def shortestFrom(graph,i):
            #print('from',i)
            crossed = {(i,1 << i)}
            fromPoint = {(i,1 << i)}
            step = 0
            while fromPoint:
                #print('fromPoint',fromPoint)
                step += 1
                newFromPoint = set()
                for p,c in fromPoint:
                    for t in graph[p]:
                        np = (t,1 << t | c)
                        #print(p,c,t,np)
                        if np[1] == allCrossed:
                            return step
                        if np not in crossed:
                            crossed.add(np)
                            newFromPoint.add(np)
                fromPoint = newFromPoint

        for i in range(n):
            ansI = shortestFrom(graph,i)
            ans = min(ans,ansI)
        return ans