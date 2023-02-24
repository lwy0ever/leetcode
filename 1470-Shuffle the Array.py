class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0] * n * 2
        for i in range(n):
            ans[i * 2] = nums[i]
            ans[i * 2 + 1] = nums[n + i]
        return ans