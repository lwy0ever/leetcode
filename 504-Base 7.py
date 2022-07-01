class Solution:
    def convertToBase7(self, num: int) -> str:
        ans = []
        sign = ''
        if num < 0:
            num = -num
            sign = '-'
        d = num
        mod = 7
        while d:
            d,m = divmod(d,mod)
            ans.append(str(m))
        if not ans:
            ans = '0'
        return sign + ''.join(reversed(ans))