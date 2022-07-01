class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        # 先用bfs,计算到达大节点需要的步数
        # 然后判断从大节点向小节点可以走的步数
        maps = collections.defaultdict(list)
        for u,v,c in edges:
            maps[u].append([v,c])
            maps[v].append([u,c])
        minStep = [float('inf')] * n    # 表示到达点minStep[i]的最小步数
        minStep[0] = 0
        # 从点0开始,h[i][0]表示最小步数,h[i][1]表示节点编号
        # 利用小根堆,减少反复检查的可能性
        h = [[0,0]]
        while h:
            step,node = heapq.heappop(h)
            for k,v in maps[node]:
                if step + v + 1 <= maxMoves and step + v + 1 < minStep[k]:
                    heapq.heappush(h,[step + v + 1,k])
                    minStep[k] = step + v + 1
        #print(minStep)
        ans = 0
        for i in range(n):
            if minStep[i] <= maxMoves:
                ans += 1
        for u,v,c in edges:
            if minStep[u] < maxMoves:
                if minStep[v] < maxMoves:
                    ans += min(maxMoves - minStep[u] + maxMoves - minStep[v],c)
                else:
                    ans += min(maxMoves - minStep[u],c)
            else:
                if minStep[v] < maxMoves:
                    ans += min(maxMoves - minStep[v],c)
        return ans
