class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        l = n // 2
        for i in range(l,-1,-1):
            for p in range(0,n - i * 2):
                if s[p:p + i] == s[p + i * 2:p + i:-1]:
                    return s[p:p + i * 2 + 1]
            for p in range(0,n - i * 2 + 1):
                if s[p:p + i] == s[p + i * 2 - 1:p + i - 1:-1]:
                    return s[p:p + i * 2]