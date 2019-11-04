class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        # dp[i][j]表示连接i,k,j点(i < k < j)组成三角形的情况下，最低得分
        n = len(A)
        inf = float('inf')
        dp = [[inf] * n for _ in range(n)]
        
        for i in range(n - 1):
            dp[i][i + 1] = 0
        
        # i 到 j 的距离(j - i)，最小为2，最大为n - 1
        for distance in range(2,n):
            for i in range(0,n - distance):
                j = i + distance
                for k in range(i + 1,j):
                    dp[i][j] = min(dp[i][j],dp[i][k] + dp[k][j] + A[i] * A[k] * A[j])
        return dp[0][n - 1]