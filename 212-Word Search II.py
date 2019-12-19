class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wd = {}
        for w in words:
            cur = wd
            for c in w:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur['#'] = w
        #print(wd)
        
        di = [(-1,0),(1,0),(0,-1),(0,1)]
        ans = set()
        n = len(board)
        m = len(board[0])

        def dfs(i,j,cur):
            #print(i,j,cur)
            #print(board)
            nonlocal ans
            ch = board[i][j]
            if ch not in cur:
                return
            cur = cur[ch]
            if '#' in cur:
                ans.add(cur['#'])
            board[i][j] = '!' # 标记为已使用
            for d in di:
                if 0 <= i + d[0] < n and 0 <= j + d[1] < m:
                    dfs(i + d[0],j + d[1],cur)
            board[i][j] = ch  # 恢复该点为可以使用
                

        for i in range(n):
            for j in range(m):
                # 由于需要多个单词同时搜索,每个字母在不同的单词间可以复用,在同一个单词的搜索时不能复用
                # 而在匹配wd的时候,甚至不知道要搜索的单词是什么
                # 因此难易标记
                # 放弃bfs,使用dfs                
                if board[i][j] in wd:
                    dfs(i,j,wd)
        return list(ans)