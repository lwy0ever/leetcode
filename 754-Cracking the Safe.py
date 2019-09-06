from collections import deque
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
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

        return ''.join(ans)