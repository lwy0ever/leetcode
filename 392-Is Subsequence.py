class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        loc = -1
        for c in s:
            loc = t.find(c,loc + 1)
            if loc == -1:
                return False
        return True