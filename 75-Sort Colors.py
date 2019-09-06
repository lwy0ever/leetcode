class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l = 0
        r = n - 1
        cur = 0
        # 保持l左侧为0
        # 保持r右侧为0
        # 位置l,r的数值需要判断
        while cur <= r:
            if nums[cur] == 0:
                nums[l],nums[cur] = nums[cur],nums[l]
                l += 1
                cur += 1
            elif nums[cur] == 1:
                cur += 1
            elif nums[cur] == 2:
                nums[cur],nums[r] = nums[r],nums[cur]
                r -= 1
