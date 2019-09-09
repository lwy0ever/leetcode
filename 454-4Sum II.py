class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        cnt = collections.Counter([a + b for b in B for a in A])
        return sum(cnt[-c - d] for d in D for c in C)