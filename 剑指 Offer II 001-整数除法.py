class Solution:
    def divide(self, a: int, b: int) -> int:
        sign = (a > 0) ^ (b > 0)
        a = abs(a)
        b = abs(b)
        cnt = 0
        # 尝试a减去b的2,4,8,16,32...倍
        while a >= b:
            b <<= 1
            cnt += 1
        ans = 0
        while cnt > 0:
            cnt -= 1
            b >>= 1
            if a >= b:
                ans += (1 << cnt)
                a -= b
        if sign:
            ans = -ans
        return 2 ** 31 - 1 if ans < - (1 << 31) or ans > (1 << 31) - 1 else ans