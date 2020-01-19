class Solution:
    def integerBreak(self, n: int) -> int:
        # 3 * 3 > 2 * 2 * 2
        base = {2:1,3:2,4:4,5:6}
        if n in base:
            return base[n]
        ans = 1
        while n - 3 >= 3:
            ans *= 3
            n -= 3
        ans *= max(base[n],n)
        return ans