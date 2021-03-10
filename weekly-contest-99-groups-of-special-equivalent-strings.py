#from collections import Counter
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        res = set()
        for sub in A:
            sub = ''.join(sorted(sub[::2]) + sorted(sub[1::2]))
            res.add(sub)
        return len(res)
        '''
        n = len(A)
        ans = n
        grouped = [False] * n
        c0 = []
        c1 = []
        for i in range(n):
            c0.append(Counter(A[i][0::2]))
            c1.append(Counter(A[i][1::2]))
        for i in range(n - 1):
            for j in range(i + 1,n):
                if grouped[j]:
                    continue
                if c0[i] == c0[j] and c1[i] == c1[j]:
                    ans -= 1
                    grouped[j] = True
        return ans
        '''