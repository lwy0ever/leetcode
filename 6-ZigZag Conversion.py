class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ''
        n = numRows
        if n == 1:
            return s
        l = len(s)
        ans += s[0::n * 2 - 2]
        for i in range(1,n - 1):
            c = 0
            while True:
                a = i + (n * 2 - 2) * c
                if a < l:
                    ans += s[a]
                else:
                    break
                b = n * 2 - 2 - i + (n * 2 - 2) * c
                if b < l:
                    ans += s[b]
                else:
                    break
                c += 1
        ans += s[n - 1::n * 2 - 2]
        return ans