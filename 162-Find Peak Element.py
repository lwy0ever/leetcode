class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 二分查找
        n = len(nums)
        if n == 1:
            return 0
        l = 0
        r = n - 1   # 因为使用mid和mid + 1进行比较,注意使用左闭右闭区间
        while l < r:
            # 查找到一个点
            mid = (l + r) // 2
            #print(mid)
            # 如果nums[mid] > nums[mid + 1],说明左侧一定有峰
            if nums[mid] > nums[mid + 1]:
                r = mid
            # 如果nums[mid] < nums[mid + 1],说明右侧一定有峰
            else:
                l = mid + 1
        return l