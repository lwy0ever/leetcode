from collections import defaultdict
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = len)
        preNumber = defaultdict(int)
        #print(words)
        for w in words:
            n = len(w)
            preS = []
            for i in range(n):
                nw = w[:i] + w[i + 1:]
                preS.append(preNumber[nw])
            preNumber[w] = max(preS) + 1
        print(preNumber)
        return max(preNumber.values())