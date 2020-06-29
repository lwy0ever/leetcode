class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [nums[0]]
        for n in nums[1:]:
            ans.append(ans[-1] + n)
        return ans