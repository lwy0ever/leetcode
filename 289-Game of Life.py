class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nb = {(i,j) for j in range(-1,2) for i in range(-1,2)}
        nb.remove((0,0))
        #print(nb)
        change = []
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            board[i].insert(0,0)
            board[i].append(0)
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


        
        
        
        