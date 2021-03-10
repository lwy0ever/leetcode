class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n == 0:
            return '0'
        ans = []
        cnt = 0
        while n > 0:
            n,m = divmod(n,10)
            ans.append(str(m))
            cnt += 1
            if cnt % 3 == 0:
                ans.append('.')
        if ans[-1] == '.':
            ans.pop()
        return ''.join(ans[::-1])