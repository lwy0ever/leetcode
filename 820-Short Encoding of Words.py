class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key = lambda x:-len(x))
        ans = 0
        es = set()
        for w in words:
            if w in es:
                continue
            for i in range(len(w)):
                if w[i:] in es:
                    break
                es.add(w[i:])
            ans += len(w) + 1
        return ans