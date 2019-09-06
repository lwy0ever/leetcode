class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rn = len(matrix)
        if rn == 0:
            return False
        cn = len(matrix[0])
        if cn == 0:
            return False
        l = 0
        r = rn * cn
        while l < r:
            m = (l + r) // 2
            row,col = divmod(m,cn)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = m + 1
            else:
                r = m
        return False