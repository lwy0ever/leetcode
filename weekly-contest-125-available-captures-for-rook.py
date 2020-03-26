class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        n = len(board)
        m = len(board[0])
        di = [(-1,0),(1,0),(0,-1),(0,1)]
        rook = (8,8)
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'R':
                    rook = (i,j)
                    break
            else:
                continue
            break
        ans = 0
        for dx,dy in di:
            step = 1
            while True:
                if 0 <= rook[0] + dx * step < n and 0 <= rook[1] + dy * step < m:
                    if board[rook[0] + dx * step][rook[1] + dy * step] == 'B':
                        break
                    elif board[rook[0] + dx * step][rook[1] + dy * step] == 'p':
                        ans += 1
                        break
                else:
                    break
                step += 1
        return ans