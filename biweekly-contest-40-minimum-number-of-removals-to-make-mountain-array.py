class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        # 找到最长上升子数组,最长下降子数组
        # todo:LIS算法时间复杂度为O(N^2),有一种O(NlogN)的算法待实现
        LIS = [1] * n   # LIS[i]表示包含nums[i]的最长上升子数组
        LDS = [1] * n   # LDS[i]表示包含nums[i]的最长下降子数组
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    LIS[i] = max(LIS[i],LIS[j] + 1)
        for i in range(n - 1,-1,-1):
            for j in range(i + 1,n):
                if nums[i] > nums[j]:
                    LDS[i] = max(LDS[i],LDS[j] + 1)
        print(LIS,LDS)
        ans = 0
        for i in range(1,n - 1):
            if LIS[i] >= 2 and LDS[i] >= 2:
                ans = max(ans,LIS[i] + LDS[i] - 1)
        return n - ans