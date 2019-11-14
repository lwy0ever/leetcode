class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        if n == 0:
            return []
        m = len(matrix[0])
        rowUp = 0
        rowDown = n - 1
        colLeft = 0
        colRight = m - 1
        ans = []
        while True:
            # 右移
            ans += [matrix[rowUp][i] for i in range(colLeft,colRight + 1)]
            rowUp += 1
            if rowUp > rowDown or colLeft > colRight:
                break
            # 下移
            ans += [matrix[i][colRight] for i in range(rowUp,rowDown + 1)]
            colRight -= 1
            if rowUp > rowDown or colLeft > colRight:
                break
            # 左移
            ans += [matrix[rowDown][i] for i in range(colRight,colLeft - 1,-1)]
            rowDown -= 1
            if rowUp > rowDown or colLeft > colRight:
                break
            # 上移
            ans += [matrix[i][colLeft] for i in range(rowDown,rowUp - 1,-1)]
            colLeft += 1
            if rowUp > rowDown or colLeft > colRight:
                break
        return ans
