class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            l = 0
            while n:
                n //= 10
                l += 1
            if l & 1 == 0:
                ans += 1
        return ans