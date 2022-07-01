class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        pre = -1
        while n:
            if n & 1 != pre:
                pre = n & 1
                n >>= 1
            else:
                return False
        return True