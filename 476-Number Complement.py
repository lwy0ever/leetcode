class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        ans = 0
        i = 0
        while num:
            if num & 1 == 0:
                ans |= (1 << i)
            num >>= 1
            i += 1
        return ans