class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # 递归吧
        n = len(nums)
        ans = set()
        def dfs(arr,ind):
            #print(arr,ind)
            if ind == n:
                if len(arr) >= 2:
                    ans.add(tuple(arr))
                return
            if (arr and nums[ind] >= arr[-1]) or not arr:
                dfs(arr + [nums[ind]],ind + 1)
            dfs(arr,ind + 1)
        
        dfs([],0)
        return list(list(x) for x in ans)