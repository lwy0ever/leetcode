class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        pre = -1
        for e in nums:
            if pre < 0:
                pre = e
            else:
                pre += e
            result = max(pre,result)
        return result
         