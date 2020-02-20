class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        d = collections.defaultdict(list)
        for i in range(n):
            d[arr[i]].append(i)
        #print(d)
        # bfs
        fromP = {0}
        visited = {0}
        ans = 0
        while (n - 1) not in fromP:
            ans += 1
            toP = set()
            for f in fromP:
                if f - 1 >= 0 and f - 1 not in visited:
                    toP.add(f - 1)
                    visited.add(f - 1)
                if f + 1 < n and f + 1 not in visited:
                    toP.add(f + 1)
                    visited.add(f + 1)
                if arr[f] in d:
                    for t in d[arr[f]]:
                        if t != f and t not in visited:
                            toP.add(t)
                            visited.add(t)
                    del d[arr[f]]
            fromP = toP
            #print(fromP)
            #print(visited)
        return ans