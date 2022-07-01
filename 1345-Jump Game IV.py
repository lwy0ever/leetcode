class Solution:
    def minJumps(self, arr: List[int]) -> int:
        target = len(arr) - 1
        d = dict()
        for i,a in enumerate(arr):
            if a in d:
                d[a].append(i)
            else:
                d[a] = [i]
        # bfs
        fromP = {0}
        visited = {0}
        step = 0
        while True:
            if target in fromP:
                return step
            toP = set()
            for f in fromP:
                if arr[f] in d:
                    for t in d[arr[f]]:
                        if t not in visited:
                            toP.add(t)
                            visited.add(t)
                    del d[arr[f]]
                if f + 1 not in visited:
                    toP.add(f + 1)
                    visited.add(f + 1)
                if f - 1 not in visited and f - 1 >= 0:
                    toP.add(f - 1)
                    visited.add(f - 1)
            fromP = toP
            #print(fromP)
            step += 1