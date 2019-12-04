class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # 优化方案
        # 利用matrix本身
        # matrix[i][j]表示以matrix[i][j]为右下角的区域,正方形的数量
        # 设dp[l][i][j]表示以(i,j)为右下角,l为长度的正方形的数量(只能为0或者1)
        # 那么dp[l][i][j] = dp[l - 1][i - 1][j - 1] and dp[l - 1][i - 1][j] and dp[l - 1][i][j - 1]
        # 所以如果matrix[i][j] == 1
        # matrix[i][j] = min(min(matrix[i - 1][j - 1],matrix[i - 1][j],matrix[i][j - 1]) + 1,其中最后的+1是由于matrix[i][j] = 1
        ans = 0
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            if matrix[i][0] == 1:
                ans += 1
        for j in range(1,m):
            if matrix[0][j] == 1:
                ans += 1
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i - 1][j - 1],matrix[i - 1][j],matrix[i][j - 1]) + 1  # 最后的+1是由于matrix[i][j] = 1
                    ans += matrix[i][j]
        return ans
                    
        '''
        n = len(matrix)
        m = len(matrix[0])
        minLen = min(m,n)
        dp = [[0] * m for _ in range(n)] # dp[l + 1][i][j]表示长度为l,起点为(i,j)的正方形是否全部为1
        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    dp[i][j] = 1
                    ans += 1
        for l in range(1,minLen):
            ndp = [[0] * (m - l) for _ in range(n - l)]
            for i in range(n - l):
                for j in range(m - l):
                    #print(l,i,j)
                    if dp[i][j] and dp[i + 1][j] and dp[i][j + 1] and dp[i + 1][j + 1]:
                        ndp[i][j] = 1
                        ans += 1
            dp = ndp
        return ans
        '''