from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lp = Counter(re.sub(r'[^*a-z]','',licensePlate.lower()))
        maxlen = 10000
        ans = ''
        for w in words:
            cnt = Counter(w)
            if cnt & lp == lp and len(w) < maxlen:
                maxlen = len(w)
                ans = w
        return ans