class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        dp = [[0] * n for _ in range(n)]    # dp[i][j]表示到达(i,j)的最大值
        m = [[0] * n for _ in range(n)]    # m[i][j]表示到达(i,j)的最大值的方案数
        dp[-1][-1] = 0
        m[-1][-1] = 1
        for i in range(n - 2,-1,-1):
            if board[n - 1][i] == 'X':
                m[n - 1][i] = 0
                dp[n - 1][i] = 0
            else:
                m[n - 1][i] = m[n - 1][i + 1]
                dp[n - 1][i] = dp[n - 1][i + 1] + int(board[n - 1][i])
            if board[i][n - 1] == 'X':
                m[i][n - 1] = 0
                dp[i][n - 1] = 0
            else:
                m[i][n - 1] = m[i + 1][n - 1]
                dp[i][n - 1] = dp[i + 1][n - 1] + int(board[i][n - 1])
        for i in range(n - 2,-1,-1):
            for j in range(n - 2,-1,-1):
                if board[i][j] == 'X':
                    m[i][j] = 0
                    dp[i][j] = 0
                else:
                    ma = max(dp[i + 1][j + 1],dp[i][j + 1],dp[i + 1][j])
                    if board[i][j] == 'E':
                        dp[i][j] = ma
                    else:
                        dp[i][j] = ma + int(board[i][j])                     
                    if dp[i + 1][j + 1] == ma:
                        m[i][j] += m[i + 1][j + 1]
                    if dp[i][j + 1] == ma:
                        m[i][j] += m[i][j + 1]
                    if dp[i + 1][j] == ma:
                        m[i][j] += m[i + 1][j]
        if m[0][0] != 0:
            return [dp[0][0],m[0][0] % (10 ** 9 + 7)]
        else:
            return [0,0]
