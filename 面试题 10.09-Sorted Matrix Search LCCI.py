class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 从右上角开始
        # cur < target,下移
        # cur > target,左移
        # 如果超出了边界,则说明无解
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        x = 0
        y = n - 1
        while matrix[x][y] != target:
            if matrix[x][y] > target:
                y -= 1
            elif matrix[x][y] < target:
                x += 1
            #print(x,y)
            if x == m or y < 0:
                return False
        return True