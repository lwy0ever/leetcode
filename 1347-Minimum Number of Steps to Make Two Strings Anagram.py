class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cntS = collections.Counter(s)
        cntT = collections.Counter(t)
        d = +(cntS - cntT)
        return sum(d.values())