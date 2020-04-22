class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        ds = [[] for _ in range(n)]
        for f,t in relation:
            ds[f].append(t)
        # bfs
        fromP = {0:1} # fromP的keys表示起始点,values表示到达这个点的方案数
        while fromP and k > 0:
            toP = collections.defaultdict(int)
            for f,v in fromP.items():
                for t in ds[f]:
                    toP[t] += v
            fromP = toP
            k -= 1
            #print(fromP)
        return fromP[n - 1]
        '''
        ds = [[] for _ in range(n)]
        for f,t in relation:
            ds[f].append(t)
        # bfs
        fromP = [0]
        while fromP and k > 0:
            toP = []
            for f in fromP:
                for t in ds[f]:
                    toP.append(t)
            fromP = toP
            k -= 1
            #print(fromP)
        if k == 0:
            return sum(p == n - 1 for p in fromP)
        else:
            return 0
        '''