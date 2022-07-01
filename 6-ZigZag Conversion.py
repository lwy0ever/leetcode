class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = [[] for _ in range(numRows)]
        cur = 0
        direct = 1
        for c in s:
            ans[cur].append(c)
            cur += direct
            if cur == -1 or cur == numRows:
                direct = - direct
                cur += direct * 2
        return ''.join(''.join(ans[i]) for i in range(numRows))