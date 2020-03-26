class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        ans = 0
        for a in arr1:
            if bisect.bisect_left(arr2,a - d) == bisect.bisect_right(arr2,a + d):
                ans += 1
        return ans