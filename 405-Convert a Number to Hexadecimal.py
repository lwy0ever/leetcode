class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        mm = '0123456789abcdef'
        if num > 0:
            d = num
        if num < 0:
            d = (2 ** 32 - 1) ^ (-num) - 1
        ans = []
        while d > 0:
            d,m = divmod(d,16)
            ans.append(mm[m])
        return ''.join(ans[::-1])
