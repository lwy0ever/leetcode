class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for i in range(start,start + n * 2,2):
            #print(i)
            ans ^= i
        return ans