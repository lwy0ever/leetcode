class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for i in range(1 << n):
            one = []
            for j in range(n):
                if 1 << j & i:
                    one.append(nums[j])
            ans.append(one)
        return ans