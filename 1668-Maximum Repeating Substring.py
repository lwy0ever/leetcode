class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = len(sequence)
        m = len(word)
        ans = 0
        for i in range(n - m + 1):
            ind = i
            tans = 0
            while sequence[ind:ind + m] == word:
                tans += 1
                ind += m
            ans = max(ans,tans)
        return ans
            