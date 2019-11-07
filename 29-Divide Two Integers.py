class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend > 0) ^ (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        cnt = 0
        while dividend >= divisor:
            cnt += 1
            divisor <<= 1
        ans = 0
        while cnt > 0:
            cnt -= 1
            divisor >>= 1
            if dividend >= divisor:
                ans += (1 << cnt)
                dividend -= divisor
        if sign:
            ans = -ans
        return (1 << 31) - 1 if ans < - (1 << 31) or ans > (1 << 31) - 1 else ans