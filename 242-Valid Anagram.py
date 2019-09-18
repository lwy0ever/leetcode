class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt1 = collections.Counter(s)
        cnt2 = collections.Counter(t)
        return cnt1 == cnt2