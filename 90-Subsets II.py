class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def dfs(arr,pos):
            ans.append(arr)
            for i in range(pos,n):
                if i > pos and nums[i] == nums[i - 1]:
                    continue
                dfs(arr + [nums[i]],i + 1)

        nums.sort()
        dfs([],0)
        return ans