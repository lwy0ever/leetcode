class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 旋转
        n = len(matrix)
        for i in range(n // 2): # 从外往内的圈数
            for j in range(i,n - 1 - i):    # 每圈的边长-1
                matrix[i][j]        ,matrix[j][n - i - 1]   ,matrix[n - i - 1][n - j - 1]   ,matrix[n - j - 1][i]       , = \
                matrix[n - j - 1][i],matrix[i][j]           ,matrix[j][n - i - 1]           ,matrix[n - i - 1][n - j - 1]

        '''
        # 先转置,再倒叙
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        #print(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j],matrix[i][n - 1 - j] = matrix[i][n - 1 - j],matrix[i][j]
        '''