class Solution:
    def longestPrefix(self, s: str) -> str:
        ans = ''
        n = len(s)
        for i in range(1,n):
            if s[:i] == s[-i:]:
                ans = s[:i]
        return ans