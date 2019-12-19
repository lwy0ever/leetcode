class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        if m == 0:
            return 0
        dp = [[0] * (m + 1) for _ in range(n + 1)]    # dp[i][j]表示以matrix[i - 1][j - 1]为右下角的正方形的最大边长
        ans = 0
        for i in range(1,n + 1):
            for j in range(1,m + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i - 1][j],dp[i][j - 1],dp[i - 1][j - 1]) + 1
                    ans = max(ans,dp[i][j])
        return ans * ans
        '''
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        if m == 0:
            return 0
        preCal = [[0] * (m + 1) for _ in range(n + 1)]    # preCal[i][j]表示(0,0)到(i - 1,j - 1)形成的矩形区域的1的数量
        for i in range(1,n + 1):
            for j in range(1,m + 1):
                preCal[i][j] = preCal[i][j - 1] + preCal[i - 1][j] - preCal[i - 1][j - 1] + int(matrix[i - 1][j - 1])
        #print(preCal)
                
        def check(length):
            #print(n,m)
            for i in range(n + 1 - length):
                for j in range(m + 1 - length):
                    if preCal[i + length][j + length] - preCal[i + length][j] - preCal[i][j + length] + preCal[i][j] == length * length:
                        return True
            return False
                
        # 二分查找最大正方形
        l = 0
        r = min(m,n)
        while l <= r:
            length = (l + r) // 2
            c = check(length)
            if c:
                l = length + 1
            else:
                r = length - 1
        return r * r
        '''