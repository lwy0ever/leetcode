class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # 二分查找
        l = 0
        r = len(arr)
        while True:
            m = (l + r) // 2
            if arr[m - 1] < arr[m] > arr[m + 1]:
                return m
            elif arr[m - 1] < arr[m] < arr[m + 1]:
                l = m
            elif arr[m - 1] > arr[m] > arr[m + 1]:
                r = m