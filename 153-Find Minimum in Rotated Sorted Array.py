class Solution:
    def findMin(self, nums: List[int]) -> int:
        #print(nums)
        n = len(nums)
        if n == 1:
            return nums[0]
        # 如果nums[0] < nums[-1],说明是正序数组
        if nums[0] < nums[-1]:
            return nums[0]
        # 如果nums[0] > nums[-1],从中间切割
        # 使用mid = (n - 1) // 2,这样:
        # n = 2,mid = 0
        # n = 3,4,mid = 1
        # ...
        mid = (n - 1) // 2
        # 退出条件,mid附近发现倒序
        # 先判断mid + 1,可以处理n = 2的情况
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        # mid + 1的判断没有通过,说明n > 2
        if nums[mid - 1] > nums[mid]:
            return nums[mid]
        if nums[0] < nums[mid]:
            # 前一半正序
            return self.findMin(nums[mid + 1:])
        else:
            # 后一半正序
            return self.findMin(nums[:mid])