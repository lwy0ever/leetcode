class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # 双指针
        n = len(nums)
        l = 0
        r = 0
        cnt0 = 0
        ans = 0
        while r < n:
            if nums[r] == 0:
                cnt0 += 1
            while cnt0 > 1:
                if nums[l] == 0:
                    cnt0 -= 1
                l += 1
            r += 1
            ans = max(ans,r - l - 1)
        return ans