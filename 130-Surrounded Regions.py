class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #print(board)
        n = len(board)
        if n == 0:
            return
        m = len(board[0])
        if m == 0:
            return
        di = ((0,-1),(0,1),(-1,0),(1,0))
        # 从边缘的O开始bfs,将O变成K(keep)
        # 将非边缘的,所有的O变成X
        # 将K恢复为O
        def bfs(x,y):
            if board[x][y] != 'O':
                return
            board[x][y] = 'K'
            fromP = {(x,y)}
            #print(board)
            while fromP:
                #print(fromP)
                toP = set()
                for x,y in fromP:
                    for dx,dy in di:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < n and 0 <= ny < m:
                            if board[nx][ny] == 'O':
                                board[nx][ny] = 'K'
                                toP.add((nx,ny))
                fromP = toP
            #print(board)

        for i in range(n):
            bfs(i,0)
            bfs(i,m - 1)
        for j in range(1,m - 1):    # (0,0)和(n - 1,m - 1)在上一个循环已经处理过
            bfs(0,j)
            bfs(n - 1,j)
        #print(board)
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'K':
                    board[i][j] = 'O'