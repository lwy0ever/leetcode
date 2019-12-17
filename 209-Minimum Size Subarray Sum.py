class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # 双指针
        n = len(nums)
        l = 0
        r = 0
        ans = n + 1
        t = 0
        while r < n:
            if t < s:
                t += nums[r]
                r += 1
            while t >= s:
                ans = min(ans,r - l)
                t -= nums[l]
                l += 1
        return ans if ans <= n else 0