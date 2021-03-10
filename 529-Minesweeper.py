class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        m = len(board)
        n = len(board[0])
        di = []
        for x in range(-1,2):
            for y in range(-1,2):
                if x == 0 and y == 0:
                    continue
                di.append((x,y))
        # bfs
        fromP = {tuple(click)}
        visited = set()
        while fromP:
            toP = set()
            for fx,fy in fromP:
                if board[fx][fy] == 'E':
                    cnt = 0
                    for dx,dy in di:
                        if 0 <= fx + dx < m and 0 <= fy + dy < n and board[fx + dx][fy + dy] == 'M':
                            cnt += 1
                    if cnt > 0:
                        board[fx][fy] = str(cnt)
                    else:
                        board[fx][fy] = 'B'
                        for dx,dy in di:
                            if 0 <= fx + dx < m and 0 <= fy + dy < n:
                                toP.add((fx + dx,fy + dy))
                    visited.add((fx,fy))
            fromP = toP
        return board
                