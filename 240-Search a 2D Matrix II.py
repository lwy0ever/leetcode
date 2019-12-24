class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])
        if m == 0:
            return False
        # 对于元素x
        # 正上方和左侧的所有元素 < x
        # 正下方和右侧的所有元素 > x
        # 并且
        # 正左侧和上方的所有元素 < x
        # 正右侧和下方的所有元素 > x
        # 左下角/右上角是接近中间值的,需要选择其一进行初始化
        col = m - 1 # 初始化在右上角
        row = 0
        while col >= 0 and row < n:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
        return False