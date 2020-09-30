class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        # 设matrix为m行n列
        # 考虑起始列为0,1,2,...n列的情况
        #     考虑中止列为0,1,2,...n列的情况
        #         从第0行开始考虑,逐行累加
        #           如果累加和为负数,则抛弃
        #           如果累加和为正数,则保留
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m)]    # dp[i][j]记录sum(matrix[i][0:j])
        for i in range(m):
            for j in range(n):
                dp[i][j + 1] = dp[i][j] + matrix[i][j]
        #print(dp)
        ma = float('-inf')
        ans = [0,0,0,0]
        for colStart in range(n):   # 考虑起始列为0,1,2,...n列的情况
            for colEnd in range(colStart,n):    # 考虑中止列为0,1,2,...n列的情况
                s = 0
                rowStart = 0
                for rowEnd in range(m): # 从第0行开始考虑,逐行累加
                    s += dp[rowEnd][colEnd + 1] - dp[rowEnd][colStart]
                    if s > ma:
                        ma = s
                        ans = [rowStart,colStart,rowEnd,colEnd]
                    if s < 0:   # 如果累加和为负数,则抛弃
                        s = 0
                        rowStart = rowEnd + 1
        return ans