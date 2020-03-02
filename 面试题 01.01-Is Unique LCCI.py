class Solution:
    def isUnique(self, astr: str) -> bool:
        mask = 0
        for c in astr:
            n = 1 << (ord(c) - ord('a'))
            if n & mask:
                return False
            mask |= n
        return True