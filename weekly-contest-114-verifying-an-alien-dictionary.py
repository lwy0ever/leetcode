class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # 把字符映射到标准字符
        index = dict()
        for i,c in enumerate(order):
            index[c] = chr(ord('a') + i)
        newWords = [''.join(index[c] for c in word) for word in words]
        #print(newWords)
        return sorted(newWords) == newWords