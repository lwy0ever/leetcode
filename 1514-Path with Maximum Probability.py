class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        dp = [0] * n    # dp[i]表示从start到i的最大概率
        dp[start] = 1
        m = len(edges)
        ft = collections.defaultdict(dict)
        for i in range(m):
            ft[edges[i][0]][edges[i][1]] = succProb[i]
            ft[edges[i][1]][edges[i][0]] = succProb[i]
        #print(ft)
        # bfs
        fromP = {start}
        while fromP:
            toP = set()
            for f in fromP:
                for t in ft[f]:
                    #print(start,f,t,dp[start][f],dp[f][t],ft[f][t],dp[start][t])
                    p = dp[f] * ft[f][t]
                    # 大于当前最大概率 and 大于已有的dp[start][end](避免无效计算)
                    if p > dp[t] and p > dp[end]:
                        dp[t] = p
                        toP.add(t)
            fromP = toP
            #print(fromP)
        #print(dp)
        return dp[end]