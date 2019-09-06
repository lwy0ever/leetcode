from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ccnt = Counter(chars)
        ans = 0
        for w in words:
            wcnt = Counter(w)
            if wcnt & ccnt == wcnt:
                ans += len(w)
        return ans