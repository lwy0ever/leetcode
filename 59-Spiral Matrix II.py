class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        cnt = 1
        rowUp = 0
        rowDown = n - 1
        colLeft = 0
        colRight = n - 1
        while cnt <= n * n:
            # 右移
            for i in range(colLeft,colRight + 1):
                ans[rowUp][i] = cnt
                cnt += 1
            rowUp += 1
            # 下移
            for i in range(rowUp,rowDown + 1):
                ans[i][colRight] = cnt
                cnt += 1
            colRight -= 1
            # 左移
            for i in range(colRight,colLeft - 1,-1):
                ans[rowDown][i] = cnt
                cnt += 1
            rowDown -= 1
            # 上移
            for i in range(rowDown,rowUp - 1,-1):
                ans[i][colLeft] = cnt
                cnt += 1
            colLeft += 1
        return ans