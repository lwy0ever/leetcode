class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # 滑动窗口
        # 如果是湍流,则继续延长
        # 如果不是湍流,则从前一个位置重新统计
        n = len(arr)
        ans = 1
        l = 0
        r = 0
        while r < n - 1:
            if l == r:
                if arr[l] == arr[l + 1]:
                    l += 1
                r += 1
            else:
                if arr[r] > arr[r - 1] and arr[r + 1] < arr[r] or arr[r] < arr[r - 1] and arr[r + 1] > arr[r]:
                    r += 1
                else:
                    l = r
            ans = max(ans,r - l + 1)
        return ans