class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0,0)}
        cur = [0,0]
        d = {'N':(0,1),'S':(0,-1),'E':(1,0),'W':(-1,0)}
        for p in path:
            cur[0] += d[p][0]
            cur[1] += d[p][1]
            t = tuple(cur)
            if t in visited:
                return True
            visited.add(t)
        return False
            