class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 滑动窗口
        n = len(nums)
        l = 0
        r = 1
        product = nums[0]
        ans = 0
        while r < n:
            while product >= k and l < r:
                product //= nums[l]
                l += 1
            # 说明nums[l:r]满足条件
            # 为了避免重复计算,只计算以r为结尾的部分
            #print(l,r,product)
            ans += (r - l)
            product *= nums[r]
            r += 1
        while product >= k and l < r:
            product //= nums[l]
            l += 1
        ans += (r - l)
        return ans
            