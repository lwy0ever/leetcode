class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        fromP = set()
        AB = [set(),set()]
        toCheck = set(range(len(graph)))
        while toCheck:
            p = toCheck.pop()
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
