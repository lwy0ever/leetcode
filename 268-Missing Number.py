class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 0...n的和 = (1 + n) * n / 2
        n = len(nums)
        return (1 + n) * n // 2 - sum(nums)
        '''
        # 做2次异或
        # 第1次从0到len(nums)
        # 第2次从nums[0]到nums[n - 1]
        n = len(nums)
        s = n
        for i in range(n):
            s ^= i
            s ^= nums[i]
        return s
        '''