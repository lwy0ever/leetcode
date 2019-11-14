class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        t = 0
        for n in nums:
            t += n
            ans = max(ans,t)
            if t < 0:
                t = 0
        return ans