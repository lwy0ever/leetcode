class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = []
        n = len(nums)
        l = 0
        r = n
        while l < r:
            m = (l + r) // 2
            if target == nums[m]:
                r = m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m
        ans.append(l if 0 <= l < n and target == nums[l] else -1)
        
        l = 0
        r = n
        while l < r:
            m = (l + r) // 2
            if target == nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m
            else:
                l = m + 1
        ans.append(l - 1 if 0 < l <= n and target == nums[l - 1] else -1)
        return ans