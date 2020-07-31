class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        columns = len(mat[0])
        # dp[i][j]表示第i行,以mat[i][j]为最右侧,最长的1 x n的矩阵长度
        dp = [[0] * columns for _ in range(rows)]
        ans = 0
        for i in range(rows):
            for j in range(columns):
                if mat[i][j]:
                    if j > 0:
                        dp[i][j] = (dp[i][j - 1] + 1)
                    else:
                        dp[i][j] = 1
                    n = float('inf')    # 表示以mat[i][j]为右下角,从第i行到第k行(行数为k - i + 1)的情况下,可以组成的矩阵的最宽列数
                    for k in range(i,-1,-1):    # 从当前行向上查找
                        n = min(n,dp[k][j]) # 表示以mat[i][j]为右下角,从第i行到第k行(行数为k - i + 1)的情况下,可以组成的矩阵的最宽列数.有多少列就有多少个矩阵
                        if n == 0:
                            break
                        ans += n
        return ans