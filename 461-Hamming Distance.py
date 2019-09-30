class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        r = x ^ y
        ans = 0
        while r:
            r &= (r - 1)
            ans += 1
        return ans