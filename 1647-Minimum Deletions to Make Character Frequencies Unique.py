class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = collections.Counter(s)
        usedFrequency = set()
        ans = 0
        for f in cnt.values():
            while f > 0 and f in usedFrequency:
                f -= 1
                ans += 1
            usedFrequency.add(f)
        return ans
            