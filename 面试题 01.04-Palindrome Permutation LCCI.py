class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        cnt = collections.Counter()
        for c in s:
            cnt[c] ^= 1
        return len(+cnt) <= 1