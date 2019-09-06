class Solution:
    def checkRecord(self, s: str) -> bool:
        a = 0
        l = 0
        for c in s:
            if c == 'A':
                a += 1
                l = 0
            elif c == 'L':
                l += 1
            else:
                l = 0
            if a > 1 or l > 2:
                return False
        return True