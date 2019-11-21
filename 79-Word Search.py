class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
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
                for d in di:
                    if 0 <= i + d[0] < n and 0 <= j + d[1] < m:
                        if (i + d[0],j + d[1]) not in visited:
                            visited.add((i + d[0],j + d[1]))
                            if dfs(i + d[0],j + d[1],pos + 1):
                                return True
                            visited.remove((i + d[0],j + d[1]))
            return False
            
        for i in range(n):
            for j in range(m):
                visited = {(i,j)}
                if dfs(i,j,0):
                    return True
        return False