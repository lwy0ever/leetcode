class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # 滑动窗口
        # 1,统计1的个数,计为m
        # 2,使用大小为m的滑动窗口,可以包含最多x个1
        # 则需要m - x次交换
        # 注意,滑动窗口需要考虑 环形数组 带来的影响
        n = len(nums)
        m = sum(nums)
        if m == n:
            return 0
        if m == 0:
            return 0
        l = 0
        r = m
        s = sum(nums[:m])
        _max = s
        for _ in range(n - 1):  # 滑动窗口需要滑动n - 1次
            #print(s)
            s += nums[r] - nums[l]
            l += 1
            r = (r + 1) % n
            _max = max(_max,s)
        return m - _max