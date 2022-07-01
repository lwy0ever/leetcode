class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans = set(nums[0])
        for l in nums:
            ans &= set(l)
            #print(ans)
        return sorted(ans)