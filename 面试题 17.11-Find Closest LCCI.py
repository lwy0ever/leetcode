class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        p1 = -1
        p2 = -1
        ans = float('inf')
        for i in range(len(words)):
            if words[i] == word1:
                p1 = i
                if p2 >= 0:
                    ans = min(ans,abs(p1 - p2))
            elif words[i] == word2:
                p2 = i
                if p1 >= 0:
                    ans = min(ans,abs(p1 - p2))
        return ans