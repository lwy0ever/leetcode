class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        arr = nums.copy()
        arr.sort()
        for n in nums:
            loc = bisect.bisect_left(arr,n)
            ans.append(loc)
        return ans