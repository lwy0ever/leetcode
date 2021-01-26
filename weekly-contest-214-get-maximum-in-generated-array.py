class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        # nums[i]
        # i为偶数时,nums[i] = nums[i // 2]
        # i为奇数时,nums[i] = nums[i // 2] + nums[i // 2 + 1]
        if n == 0:
            return 0
        nums = [0] * (n + 1)
        nums[1] = 1
        for i in range(2,n + 1):
            if i & 1:
                nums[i] = nums[i // 2] + nums[i // 2 + 1]
            else:
                nums[i] = nums[i // 2]
        return max(nums)