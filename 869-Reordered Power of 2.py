class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        cnt = collections.Counter(str(N))
        return any(cnt == collections.Counter(str(1 << i)) for i in range(31))
