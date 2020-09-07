class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        queen = []  # queen[i]表示queen在第i行的位置
        cols = 0    # 表示不能放置的列,以二进制表示
        left = 0    # 表示当前行,被所有queen影响的左下方的位置,left = 上一行的left << 1
        right = 0   # 表示当前行,被所有queen影响的右下方的位置,right = 上一行的right >> 1
        ans = []

        def dfs(row,cols,left,right):   # 尝试第row行
            #print(queen,row,bin(cols),bin(left),bin(right))
            if row == n:
                ans.append(['.' * q + 'Q' + '.' * (n - 1 - q) for q in queen])
                return
            for i in range(n):
                if (1 << i) & cols == 0 and (1 << i) & left == 0 and (1 << i) & right == 0:
                    queen.append(i)
                    dfs(row + 1,cols | (1 << i),(left | (1 << i)) << 1,(right | (1 << i)) >> 1)
                    queen.pop()

        dfs(0,0,0,0)
        return ans