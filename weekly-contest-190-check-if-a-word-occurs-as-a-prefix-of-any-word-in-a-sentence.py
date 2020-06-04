class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        ans = -1
        n = len(searchWord)
        for i,w in enumerate(sentence.split()):
            if w[:n] == searchWord:
                ans = i + 1
                return ans
        return ans