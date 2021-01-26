class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j =  n - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            #print(i,j)
            nums[i],nums[j] = nums[j],nums[i]
        nums[i + 1:] = nums[i + 1:][::-1]