class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # nb表示8个相邻格子的相对坐标
        nb = {(i,j) for j in range(-1,2) for i in range(-1,2)}
        nb.remove((0,0))
        # 在原地修改,2表示活变死,3表示死变活
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                cnt = 0
                for n in nb:
                    if 0 <= i + n[0] < rows and 0 <= j + n[1] < cols:
                        if board[i + n[0]][j + n[1]] in (1,2):
                            cnt += 1
                if board[i][j] == 1 and (cnt < 2 or cnt > 3):   # 活变死
                    board[i][j] = 2
                if board[i][j] == 0 and cnt == 3:   # 死变活
                    board[i][j] = 3
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 2:
                    board[i][j] = 0
                if board[i][j] == 3:
                    board[i][j] = 1
        '''
        # nb表示8个相邻格子的相对坐标
        nb = {(i,j) for j in range(-1,2) for i in range(-1,2)}
        nb.remove((0,0))
        #print(nb)
        # change记录需要变更的格子坐标和变更后的状态
        change = []
        rows = len(board)
        cols = len(board[0])
        # 添加左右边框
        for i in range(rows):
            board[i].insert(0,0)
            board[i].append(0)
        # 添加上下边框
        board.insert(0,[0] * (cols + 2))
        board.append([0] * (cols + 2))
        for i in range(1,rows + 1):
            for j in range(1,cols + 1):
                counter = 0
                for n in nb:
                    #print(i , n[0],j , n[1])
                    if board[i + n[0]][j + n[1]] == 1:
                        counter += 1
                if board[i][j] == 1 and (counter < 2 or counter > 3):
                    change.append((i,j,0))
                if board[i][j] == 0 and counter == 3:
                    change.append((i,j,1))
        for r,c,v in change:
            board[r][c] = v
        board.pop()
        board.pop(0)
        for i in range(rows):
            board[i].pop()
            board[i].pop(0)
        '''