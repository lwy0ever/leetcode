class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = []
        stack = []
        for v in nums[::-1]:
            p = bisect.bisect_left(stack,v)
            bisect.insort_left(stack,v)
            ans.append(p)
        return ans[::-1]