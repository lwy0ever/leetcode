class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n = len(mat)
        m = len(mat[0])
        preCal = [[0] * (m + 1) for _ in range(n + 1)]  # preCal[i][j]表示前i行,前j列组成的矩形区域内的数据和
        for i in range(1,n + 1):
            for j in range(1,m + 1):
                preCal[i][j] = preCal[i - 1][j] + preCal[i][j - 1] - preCal[i - 1][j - 1] + mat[i - 1][j - 1]
        
        def check(l):
            for i in range(n - l + 1):
                for j in range(m - l + 1):
                    if preCal[i + l][j + l] - preCal[i + l][j] - preCal[i][j + l] + preCal[i][j] <= threshold:
                        return True
            return False
        
        # 长度部分,用二分查找,提高效率
        minLen = 0
        maxLen = min(m,n)
        while minLen <= maxLen:
            l = (minLen + maxLen) // 2
            if check(l):
                minLen = l + 1
            else:
                maxLen = l - 1
        return maxLen