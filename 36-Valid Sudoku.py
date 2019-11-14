class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        for i in range(n):
            h = set()   # 横向
            v = set()   # 纵向
            for j in range(n):
                if board[i][j] != '.':
                    if board[i][j] in h:
                        return False
                    h.add(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] in v:
                        return False
                    v.add(board[j][i])
        for i in range(n // 3):
            for j in range(n // 3):
                s = set()
                for l in range(3):
                    for m in range(3):
                        if board[i * 3 + l][j * 3 + m] != '.':
                            if board[i * 3 + l][j * 3 + m] in s:
                                return False
                            s.add(board[i * 3 + l][j * 3 + m])
        return True