class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        pre = nums[0]
        i = 1
        while i < n:
            if nums[i] == pre:
                nums.pop(i)
                n -= 1
            else:
                pre = nums[i]
                i += 1
        return n