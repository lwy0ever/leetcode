class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        h = [set() for _ in range(9)]   # 横向
        v = [set() for _ in range(9)]   # 纵向
        box = [[set() for _ in range(3)] for _ in range(3)]   # 3x3
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    h[i].add(board[i][j])
                    v[j].add(board[i][j])
                    box[i // 3][j // 3].add(board[i][j])
        #print(h)
        #print(v)
        #print(b)
        n = [str(i) for i in range(1,10)]
        
        def fill(pos):
            if pos == 81:
                return True
            i,j = divmod(pos,9)
            if board[i][j] == '.':
                for t in n:
                    if t in h[i] or t in v[j] or t in box[i // 3][j // 3]:
                        continue
                    h[i].add(t)
                    v[j].add(t)
                    box[i // 3][j // 3].add(t)
                    board[i][j] = t
                    #print(pos,t,board)
                    if fill(pos + 1):
                        return True
                    h[i].remove(t)
                    v[j].remove(t)
                    box[i // 3][j // 3].remove(t)
                else:
                    board[i][j] = '.'
                    return False
            else:
                return fill(pos + 1)
        
        fill(0)