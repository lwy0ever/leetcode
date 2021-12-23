class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        ans = 0
        i = 0
        while n:
            if n & 1 == 0:
                ans |= (1 << i)
            n >>= 1
            i += 1
        return ans