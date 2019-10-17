class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # 将times变得hashable
        ts = {}
        for u,v,t in times:
            if u not in ts:
                ts[u] = {}
            ts[u][v] = t

        visited = {K:0}
        fromP = {K:0}
        while fromP:
            toP = {}
            for u in fromP:
                if u in ts:
                    for v in ts[u]:
                        if v not in visited:
                            if v not in toP:
                                toP[v] = fromP[u] + ts[u][v]
                                visited[v] = fromP[u] + ts[u][v]
                        else:   # 检查到达该点的值是否是当前最少时间
                            if visited[v] > fromP[u] + ts[u][v]:    # 不是最少时间,更新该结点及以后的节点
                                toP[v] = fromP[u] + ts[u][v]
                                visited[v] = fromP[u] + ts[u][v]
            #print(fromP)
            #print(toP)
            #print(visited)
            fromP = toP
        if len(visited) == N:
            return max(visited.values())
        else:
            return -1