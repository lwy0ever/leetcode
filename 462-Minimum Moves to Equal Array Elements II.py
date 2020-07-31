class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # 当 x 为这 N 个数的中位数时,可以使得距离和最小
        nums.sort()
        n = len(nums)
        #mid = (n - 1) // 2
        ans = 0
        l = 0
        r = n - 1
        while l < r:
            # ans += (nums[mid] - nums[l]) + (nums[r] - nums[mid])
            ans += nums[r] - nums[l]
            l += 1
            r -= 1
        return ans