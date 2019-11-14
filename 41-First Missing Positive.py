class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # 结果一定在[1,n + 1]之间
        s = {i for i in range(1,n + 2)}
        for num in nums:
            s.discard(num)
        for i in range(1,n + 2):
            if i in s:
                return i