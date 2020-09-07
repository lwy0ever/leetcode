class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def cnt(c):
            return sum(board[i].count(c) for i in range(3))
        
        def isWin(c):
            # 行
            for i in range(3):
                if board[i] == c * 3:
                    return True
            # 列
            for i in range(3):
                if all(board[j][i] == c for j in range(3)):
                    return True
            # 对角线
            if all(board[i][i] == c for i in range(3)) or all(board[i][2 - i] == c for i in range(3)):
                return True
            return False
        o = cnt('O')
        x = cnt('X')
        owin = isWin('O')
        xwin = isWin('X')
        if owin and xwin:   # 不可能都胜
            return False
        elif xwin:    # 只有x胜,则x比o多1个
            return x - 1 == o
        elif owin:    # 只有o胜,则x和o一样多
            return x == o
        else:   # 都不胜
            return x in (o,o + 1)