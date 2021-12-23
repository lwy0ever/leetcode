class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # 排序+滑动窗口
        nums.sort()
        n = len(nums)
        l = 0
        ans = 1 # 最小频次是1
        ttl = 0
        for r in range(1,n):
            # 从l到r - 1已经变得一样了
            # 将所有元素变成r需要r - l次操作
            ttl += (nums[r] - nums[r - 1]) * (r - l)
            while ttl > k:
                ttl -= nums[r] - nums[l]
                l += 1
            ans = max(ans,r - l + 1)
        return ans