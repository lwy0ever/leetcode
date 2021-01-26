class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 双指针
        # 一个指针指向最后一个非0元素的下一个位置
        # 另一个指针遍历数组,将非0元素追加到前一个指针处
        lastNonZeroFoundAt = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != lastNonZeroFoundAt:
                    nums[lastNonZeroFoundAt],nums[i] = nums[i],nums[lastNonZeroFoundAt]
                lastNonZeroFoundAt += 1
        '''
        cnt = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                cnt += 1
            else:
                i += 1
        nums += [0] * cnt
        '''