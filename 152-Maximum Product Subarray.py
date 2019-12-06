class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 包含前一个元素的contiguous subarray的最大值为ma
        # 由于存在负数,会使最大变最小,最小变最大,因此需要再保存一个最小值mi
        ans = ma = mi = nums[0]
        for n in nums[1:]:
            if n < 0:
                ma,mi = mi,ma
            ma = max(ma * n,n)
            mi = min(mi * n,n)
            ans = max(ans,ma)
        return ans