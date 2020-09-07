class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp[i][j]表示i个1,j个0,最多可以组成的数量
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        # 对于有x个1,y个0组成的字符串
        # 转移方程:dp[i][j] = max(dp[i][j],dp[i - x][j - y] + 1)
        for s in strs:
            cnt = collections.Counter(s)
            c0 = cnt['0']
            c1 = cnt['1']
            #print(s)
            for i in range(n,c1 - 1,-1):    # 这里要倒序,避免一个字符串被多次考虑
                for j in range(m,c0 - 1,-1):
                    #print(i - c1,j - c0,i,j,dp[i - c1][j - c0],dp[i][j])
                    dp[i][j] = max(dp[i][j],dp[i - c1][j - c0] + 1)
            #print(dp)
        return dp[n][m]