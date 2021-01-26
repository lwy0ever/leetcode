class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # ans[i] = nums[i] * i - sum(nums[:i]) + sum(nums[i + 1:]) - nums[i] * (n - i - 1)
        right = sum(nums)
        n = len(nums)
        ans = [0] * n
        left = 0
        for i in range(n):
            right -= nums[i]
            ans[i] = nums[i] * i - left + right - nums[i] * (n - i - 1)
            left += nums[i]
        return ans