class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse = True)
        s = sum(nums)
        ans = []
        t = 0
        for n in nums:
            ans.append(n)
            t += n
            if t * 2 > s:
                return ans            