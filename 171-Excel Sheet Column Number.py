class Solution:
    def titleToNumber(self, s: str) -> int:
        # ord('A') = 65
        ans = 0
        for c in s:
            ans = ans * 26 + (ord(c) - 64)
        return ans