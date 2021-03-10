class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        d = collections.defaultdict(list)
        for f,t in edges:
            d[t].append(f)
        ans = []
        visited = set()
        for i in range(n):
            if i in visited:
                continue
            # bfs
            fromP = {i}
            visited.add(i)
            while fromP:
                toP = set()
                for f in fromP:
                    if f not in d:
                        ans.append(f)
                        continue
                    for t in d[f]:
                        if t not in visited:
                            toP.add(t)
                            visited.add(t)
                fromP = toP
        return ans
            