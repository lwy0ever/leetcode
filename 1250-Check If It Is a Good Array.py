class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        ans = nums[0]
        for a in nums:
            ans = gcd(ans, a)
        return ans == 1