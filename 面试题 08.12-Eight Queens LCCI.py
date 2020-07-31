class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 每行的状态用二进制数表示
        ans = []    # 记录所有结果
        pos = [-1] * n # 长度n,pos[i]表示第i行皇后的位置
        def output(pos):
            one = []
            for i in range(n):
                one.append('.' * pos[i] + 'Q' + '.' * (n - pos[i] - 1))
                #print(pos[i],one[-1])
            ans.append(one)
        def t(row,cols,left,right): # 尝试第row行,其中cols已经被占用,左对角线left(归集到第0行)已经被占用,右对角线right(归集到第0行)已经被占用
            if row == n:
                output(pos)
                return
            for i in range(n):
                if i not in cols and (i + row) not in left and (i - row) not in right:
                    pos[row] = i
                    t(row + 1,cols.union({i}),left.union({i + row}),right.union({i - row}))
        t(0,set(),set(),set())
        return ans