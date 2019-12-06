class Solution:
    def findMin(self, nums: List[int]) -> int:
        #print(nums)
        n = len(nums)
        if n == 1:
            return nums[0]
        # 如果nums[0] < nums[-1],说明是正序数组
        if nums[0] < nums[-1]:
            return nums[0]
        mid = (n - 1) // 2
        if nums[mid - 1] > nums[mid]:
            return nums[mid]
        if nums[mid] > nums[-1]:
            # 前一半正序
            return self.findMin(nums[mid + 1:])
        elif nums[mid] < nums[-1]:
            # 后一半正序
            return self.findMin(nums[:mid])
        else:   # nums[mid] == nums[right]
            # 无法判断,去掉最后一个重复数据
            return self.findMin(nums[:-1])