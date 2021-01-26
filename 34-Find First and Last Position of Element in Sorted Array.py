class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 二分查找
        ans = []
        n = len(nums)
        # 先找开始位置
        l = 0
        r = n
        while l < r:
            m = (l + r) // 2
            if target <= nums[m]:
                r = m
            elif target > nums[m]:
                l = m + 1
        ans.append(l if 0 <= l < n and target == nums[l] else -1)
        # 如果没有开始位置,也就没有结束位置
        if ans[0] == -1:
            return [-1,-1]
        
        # 找结束位置
        l = 0
        r = n
        while l < r:
            m = (l + r) // 2
            if target >= nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m
        ans.append(l - 1 if 0 < l <= n and target == nums[l - 1] else -1)
        return ans