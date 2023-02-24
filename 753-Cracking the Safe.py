class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        '''
        # 以前自己写的?
        ans = ['0'] * n
        visited = {'0'*(n-1):{'0'}}
        prefix = deque(ans[1:],maxlen = n - 1)
        chars = [str(i) for i in range(k-1,-1,-1)] # the order is necessary,
        for i in range(1,k**n+1):
            s = ''.join(prefix)
            if s not in visited:
                visited[s] = set()
            for j in chars:
                if j not in visited[s]:
                    ans.append(j)
                    visited[s].add(j)
                    prefix.append(j)
                    break
        #print(visited,prefix,ans)

        return ''.join(ans)'''

        # copy官方题解
        # dfs + 暴力
        visited = set()
        ans = list()
        mod = 10 ** (n - 1)

        def dfs(tail):
            for i in range(k):
                nt = tail * 10 + i
                if nt not in visited:
                    # 先add visited
                    # 然后dfs
                    # 最后才add ans
                    # 相当于ans是倒序的
                    # ?所以最后补n - 1个0
                    visited.add(nt)
                    dfs(nt % mod)
                    ans.append(str(i))

        dfs(0)
        return ''.join(ans) + '0' * (n - 1)