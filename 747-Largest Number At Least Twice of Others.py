class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        # 记录最大值和次大值,以及最大值出现的位置
        maxIndex = 0
        maxValue = float('-inf')
        max2Value = float('-inf')
        for i,n in enumerate(nums):
            if n > maxValue:
                max2Value = maxValue
                maxValue = n
                maxIndex = i
            else:   # n <= maxValue
                if n >= max2Value:
                    max2Value = n
        return maxIndex if maxValue >= max2Value * 2 else -1