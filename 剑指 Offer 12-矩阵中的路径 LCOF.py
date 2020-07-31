class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 通过改变board的值,标记被访问的情况
        di = ((0,1),(1,0),(-1,0),(0,-1))
        n = len(board)
        m = len(board[0])
        # dfs
        # 查找board[i][j],和word[pos]匹配
        def dfs(i,j,pos):
            if board[i][j] == word[pos]:
                #print(i,j,pos,word[pos])
                t = board[i][j]
                board[i][j] = '.'   # 估计board中不包含'.'
                if pos == len(word) - 1:
                    return True
                for x,y in di:
                    if 0 <= i + x < n and 0 <= j + y < m:
                            if dfs(i + x,j + y,pos + 1):
                                return True
                board[i][j] = t
            return False
            
        for i in range(n):
            for j in range(m):
                if dfs(i,j,0):
                    return True
        return False

        # 使用set记录被访问过的位置
        '''
        di = ((0,1),(1,0),(-1,0),(0,-1))
        n = len(board)
        m = len(board[0])
        # dfs
        # 查找board[i][j],和word[pos]匹配
        def dfs(i,j,pos):
            if board[i][j] == word[pos]:
                #print(i,j,pos,word[pos])
                if pos == len(word) - 1:
                    return True
                for x,y in di:
                    if 0 <= i + x < n and 0 <= j + y < m and (i + x,j + y) not in visited:
                            visited.add((i + x,j + y))
                            if dfs(i + x,j + y,pos + 1):
                                return True
                            visited.remove((i + x,j + y))
            return False
            
        for i in range(n):
            for j in range(m):
                visited = {(i,j)}
                if dfs(i,j,0):
                    return True
        return False
        '''