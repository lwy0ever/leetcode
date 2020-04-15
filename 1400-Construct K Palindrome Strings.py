class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if k > n:
            return False
        cnt = collections.Counter(s)
        odds = 0
        for v in cnt.values():
            if v & 1:
                odds += 1
        if odds > k:
            return False
        return True