class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        is_col_0_has_original_zero = False
        r = len(matrix)
        c = len(matrix[0])
        for i in range(r):
            if matrix[i][0] == 0:
                is_col_0_has_original_zero = True
            for j in range(1,c):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for j in range(1,c):
            if matrix[0][j] == 0:
                for i in range(r):
                    matrix[i][j] = 0

        for i in range(r):
            if matrix[i][0] == 0:
                for j in range(1,c):
                    matrix[i][j] = 0

        if is_col_0_has_original_zero:
            for i in range(r):
                matrix[i][0] = 0