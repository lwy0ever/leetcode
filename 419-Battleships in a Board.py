class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # 寻找一个战舰的头部
        # 假设:上下放置的战舰,上为头;左右放置的战舰,左为头
        # 那么非头部的X,上方或者左边必然有一个是X        
        n = len(board)
        m = len(board[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'X':
                    if i > 0 and board[i - 1][j] == 'X':
                        continue
                    if j > 0 and board[i][j - 1] == 'X':
                        continue
                    ans += 1
        return ans