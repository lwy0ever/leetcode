class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        direct = collections.defaultdict(list)
        Rdirect = collections.defaultdict(list)
        for t,f in connections:
            direct[f].append(t)
            Rdirect[t].append(f)
        #print(direct)
        #print(Rdirect)
        ans = 0
        # bfs
        visited = {0}
        toP = [0]
        while toP:
            newP = []
            for t in toP:
                for f in direct[t]:
                    if f not in visited:
                        visited.add(f)
                        newP.append(f)
                for f in Rdirect[t]:
                    if f not in visited:
                        visited.add(f)
                        newP.append(f)
                        ans += 1
            toP = newP
            #print(toP,ans)
        return ans