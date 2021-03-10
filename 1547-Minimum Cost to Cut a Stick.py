class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # 为了方便处理,在cuts前后添加0和n
        # dp[i][j]表示cuts[i]和cuts[j]区间内,cut的最小成本
        # dp[i][i + 1] = 0
        cuts.sort()
        cuts = [0] + cuts + [n]
        cn = len(cuts)
        #print(cn)
        dp = [[0] * cn for _ in range(cn)]
        for l in range(2,cn):   # dp[i][j]中j - i定义为l
            for i in range(cn - l):
                j = i + l
                dp[i][j] = n * cn   # 最长不会超过n * cn
                for m in range(i + 1,j):
                    #print(i,m,j)
                    dp[i][j] = min(dp[i][j],cuts[j] - cuts[i] + dp[i][m] + dp[m][j])
        #print(dp)
        return dp[0][cn - 1]
                