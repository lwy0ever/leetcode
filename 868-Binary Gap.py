class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        ind = 0
        pre1pos = float('inf')
        while n:
            if n & 1:
                ans = max(ans,ind - pre1pos)
                pre1pos = ind
            n >>= 1
            ind += 1
        return ans