class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        idx = 1
        for i in range(1,n):
            if nums[i] == nums[i - 1]:
                ans -= 1
            else:
                nums[idx] = nums[i]
                idx += 1
        return ans
