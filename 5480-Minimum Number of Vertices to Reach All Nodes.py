class Solution:\u000A    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) \u002D\u003E List[int]:\u000A        d \u003D collections.defaultdict(list)\u000A        for f,t in edges:\u000A            d[t].append(f)\u000A        ans \u003D []\u000A        visited \u003D set()\u000A        for i in range(n):\u000A            if i in visited:\u000A                continue\u000A            # bfs\u000A            fromP \u003D {i}\u000A            visited.add(i)\u000A            while fromP:\u000A                toP \u003D set()\u000A                for f in fromP:\u000A                    if f not in d:\u000A                        ans.append(f)\u000A                        continue\u000A                    for t in d[f]:\u000A                        if t not in visited:\u000A                            toP.add(t)\u000A                            visited.add(t)\u000A                fromP \u003D toP\u000A        return ans\u000A            