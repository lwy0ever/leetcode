class Solution:
    def printVertically(self, s: str) -> List[str]:
        arr = s.split()
        _max = max([len(x) for x in arr])
        ans = [''] * _max
        for x in arr:
            for i in range(_max):
                if i >= len(x):
                    ans[i] = ans[i] + ' '
                else:
                    ans[i] = ans[i] + x[i]
        for i in range(_max):
            ans[i] = ans[i].rstrip()
        return ans