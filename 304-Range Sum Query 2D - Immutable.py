class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        if n == 0:
            return
        m = len(matrix[0])
        self.dp = [[0] * (m + 1) for _ in range(n + 1)] # dp[i][j]表示matrix(0,0)到(i,j)的区域和
        for i in range(n):
            rowSum = 0
            for j in range(m):
                rowSum += matrix[i][j]
                self.dp[i + 1][j + 1] = self.dp[i][j + 1] + rowSum
        #print(self.dp)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1] - self.dp[row2 + 1][col1] - self.dp[row1][col2 + 1] + self.dp[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)