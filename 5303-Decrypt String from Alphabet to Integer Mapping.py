class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = ''
        n = len(s)
        i = 0
        while i < n:
            if i + 2 < n and s[i + 2] == '#':
                ans += chr(int(s[i:i + 2]) + 96)
                i += 3
            else:
                ans += chr(ord(s[i]) + 48)
                i += 1
        return ans