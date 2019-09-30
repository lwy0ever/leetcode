from collections import Counter
class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        ttl = Counter(S)
        cnt = Counter()
        ans = min(ttl['0'],ttl['1'])
        for c in S:
            cnt[c] += 1
            ans = min(ans,(ttl - cnt)['0'] + cnt['1'])
        return ans