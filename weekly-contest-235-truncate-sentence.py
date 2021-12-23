class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        #return ' '.join(s.split(' ')[:k])
        i = 0
        n = len(s)
        while i < n:
            if s[i] == ' ':
                k -= 1
                if k == 0:
                    break
            i += 1
        return s[:i]