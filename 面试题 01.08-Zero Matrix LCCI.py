class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # matrix[0][i] == 0表示第i列需要清0
        # matrix[i][0] == 0表示第i行需要清0
        # matrix[0][0]需要特别标记
        m = len(matrix)
        n = len(matrix[0])
        col0 = False    # 表示第一列为0
        row0 = False    # 表示第一行为0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        row0 = True
                    if j == 0:
                        col0 = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1,m):
            if matrix[i][0] == 0:
                for j in range(1,n):
                    matrix[i][j] = 0
        for j in range(1,n):
            if matrix[0][j] == 0:
                for i in range(1,m):
                    matrix[i][j] = 0
        if col0:
            for i in range(1,m):
                matrix[i][0] = 0
        if row0:
            for j in range(1,n):
                matrix[0][j] = 0