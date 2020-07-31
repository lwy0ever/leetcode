class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 利用nums[i]记录数字i + 1是否出现过
        # 如果出现过,则nums[i]记录为负数
        n = len(nums)
        for i in range(n):
            ind = abs(nums[i]) - 1  # 当前数字应该在的位置
            if nums[ind] > 0:   # 之前没有出现过
                nums[ind] *= -1 # 记录这个位置
        ans = []
        for i in range(n):
            if nums[i] > 0:
                ans.append(i + 1)
        return ans

        # 尝试把数字归位
        '''
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1],nums[i] = nums[i],nums[nums[i] - 1]
            else:
                i += 1
        ans = []
        for i in range(n):
            if nums[i] != i + 1:
                ans.append(i + 1)
        return ans
        '''