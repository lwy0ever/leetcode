class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        n = len(s)
        s = list(s)
        l = 0
        r = n - 1
        while l < r:
            while s[l] not in vowels and l < r:
                l += 1
            while s[r] not in vowels and l < r:
                r -= 1
            if l < r:
                s[l],s[r] = s[r],s[l]
                l += 1
                r -= 1
        return ''.join(s)