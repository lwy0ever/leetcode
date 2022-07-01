class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # 排序 + 滑动窗口
        nums.sort()
        #print(nums)
        ans = float('inf')
        for i in range(len(nums) - k + 1):
            ans = min(ans,nums[i + k - 1] - nums[i])
        return ans