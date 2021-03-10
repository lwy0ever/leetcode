class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # 倒序,二分查找+插入
        ans = 0
        arr = []
        for n in nums[::-1]:
            pos = bisect.bisect_left(arr,n)
            bisect.insort_left(arr,n)
            ans += pos
        return ans