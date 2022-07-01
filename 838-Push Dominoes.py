class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # 广度优先搜索
        # 方法2:通过hash优化效率
        n = len(dominoes)
        ls = set()
        rs = set()
        ans = []
        for i,c in enumerate(dominoes):
            if c == 'L':
                ls.add(i)
            elif c == 'R':
                rs.add(i)
            ans.append(c)
        while ls or rs:
            newLs = set()
            newRs = set()
            for i in ls:
                if i >= 1:
                    if ans[i - 1] == '.' and i - 2 not in rs:
                        ans[i - 1] = 'L'
                        newLs.add(i - 1)
            for i in rs:
                if i < n - 1:
                    if ans[i + 1] == '.' and i + 2 not in ls:
                        ans[i + 1] = 'R'
                        newRs.add(i + 1)
            ls = newLs
            rs = newRs
        return ''.join(ans)        
        
        # 广度优先搜索
        # 方法1
        '''
        n = len(dominoes)
        ans = ['x'] * n
        ls = []
        rs = []
        for i,c in enumerate(dominoes):
            if c == 'L':
                ls.append(i)
                ans[i] = 'L'
            elif c == 'R':
                rs.append(i)
                ans[i] = 'R'
        while ls or rs:
            newLs = []
            newRs = []
            for i in ls:
                if i >= 1:
                    if ans[i - 1] == 'x':
                        ans[i - 1] = 'l'    # 小l表示暂定
                        newLs.append(i - 1)
            for i in rs:
                if i < n - 1:
                    if ans[i + 1] == 'x':
                        ans[i + 1] = 'R'
                        newRs.append(i + 1)
                    elif ans[i + 1] == 'l':
                        ans[i + 1] = '.'
            for i in ls:
                if i >= 1:
                    if ans[i - 1] == 'l':
                        ans[i - 1] = 'L'
            ls = newLs
            rs = newRs
            #print(''.join(ans))
        for i in range(n):
            if ans[i] == 'x':
                ans[i] = '.'
        return ''.join(ans)
        '''