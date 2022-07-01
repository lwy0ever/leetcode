class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        # hash
        wordsIndex = collections.defaultdict(list)
        for i,w in enumerate(words):
            wordsIndex[w].append(i)
        ans = float('inf')
        p1 = 0
        p2 = 0
        # 双指针
        while p1 < len(wordsIndex[word1]) and p2 < len(wordsIndex[word2]):
            ans = min(ans,abs(wordsIndex[word1][p1] - wordsIndex[word2][p2]))
            if wordsIndex[word1][p1] < wordsIndex[word2][p2]:
                p1 += 1
            else:
                p2 += 1
        return ans