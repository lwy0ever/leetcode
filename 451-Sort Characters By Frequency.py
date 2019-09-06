from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        ans = ''
        for k,v in cnt.most_common():
            ans += v * k
        return ans