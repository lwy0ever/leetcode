class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        n = len(word2)
        wInd = 0
        cInd = 0
        for w1 in word1:
            for c1 in w1:
                if wInd == n or c1 != word2[wInd][cInd]:
                    return False
                cInd += 1
                if cInd == len(word2[wInd]):
                    wInd += 1
                    cInd = 0
        return wInd == n and cInd == 0