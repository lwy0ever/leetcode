class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n
        while l < r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m
            else:
                l = m + 1
        return l