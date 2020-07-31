class Solution:
    def cuttingRope(self, n: int) -> int:
        # 3 * 3 > 2 * 2 * 2
        base = {2:1,3:2,4:4,5:6}
        if n in base:
            return base[n]
        # n >= 6
        d,m = divmod(n - 3,3)
        ans = 3 ** d
        ans *= max(base[m + 3],m + 3)
        return ans