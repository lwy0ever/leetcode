class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set()
        fromP = {start}
        # bfs
        while fromP:
            toP = set()
            for f in fromP:
                if arr[f] == 0:
                    return True
                if f not in visited:
                    visited.add(f)
                    if 0 <= f + arr[f] < n:
                        toP.add(f + arr[f])
                    if 0 <= f - arr[f] < n:
                        toP.add(f - arr[f])
            fromP = toP
        return False