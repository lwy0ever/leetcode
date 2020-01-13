class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # 预计算:presum = sum(nums[:i])
        n = len(nums)
        presum = [0] * (n + 1)
        for i in range(n):
            presum[i + 1] = presum[i] + nums[i]
        # 如果sum(nums[i:j])满足条件lower <= presum[j] - presum[i] <= upper,则区间(i,j)满足条件
        # 条件调整为presum[j] - upper <= presum[i] <= presum[j] - lower
        # 也就是在j的时候,找到区间[presum[j] - upper,presum[j] - lower]的数量,可以利用二分查找
        ans = 0
        ps = [0]
        for i in range(1,n + 1):
            left = bisect.bisect_left(ps,presum[i] - upper)
            right = bisect.bisect_right(ps,presum[i] - lower)
            ans += right - left
            bisect.insort(ps, presum[i])
        return ans