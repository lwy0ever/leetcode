class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        d = collections.defaultdict(set)
        for f,t in graph:
            d[f].add(t)
        # bfs
        '''
        fromP = {start}
        visited = {start}
        while fromP:
            toP = set()
            for f in fromP:
                for t in d[f]:
                    if t not in visited:
                        toP.add(t)
                        visited.add(t)
                #toP.update(d[f])
                #toP.difference_update(visited)
            if target in toP:
                return True
            #visited.update(toP)
            fromP = toP
        return False
        '''
        # dfs
        visited = set()
        def dfs(f):
            if f in visited:
                return False
            if f == target:
                return True
            visited.add(f)
            for t in d[f]:
                if dfs(t):
                    return True
            return False
        return dfs(start)