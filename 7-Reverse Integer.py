class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            ans = -int(str(x)[:0:-1])
        else:
            ans = int(str(x)[::-1])
        return 0 if ans > 2 ** 31 - 1 or ans < - 2 ** 31 else ans
