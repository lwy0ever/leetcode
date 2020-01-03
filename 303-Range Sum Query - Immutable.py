class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.dp = [0] * (n + 1) # dp[i] 表示nums[:i]的和
        for i,n in enumerate(nums):
            self.dp[i + 1] = self.dp[i] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j + 1] - self.dp[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)