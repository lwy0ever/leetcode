class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def sss(t):
            r = 0
            while t:
                t,m = divmod(t,10)
                r += m
            return r

        di = [(-1,0),(1,0),(0,-1),(0,1)]
        # bfs
        ans = 1
        fromP = {(0,0)}
        visited = {(0,0)}
        while fromP:
            toP = set()
            for frow,fcol in fromP:
                for dr,dc in di:
                    tr,tc = frow + dr,fcol + dc
                    if 0 <= tr < m and 0 <= tc < n:
                        _sum = sss(tr) + sss(tc)
                        if _sum > k:
                            continue
                        if (tr,tc) not in visited:
                            toP.add((tr,tc))
                            visited.add((tr,tc))
                            ans += 1
            fromP = toP
            #print(fromP)
            #break
        return ans