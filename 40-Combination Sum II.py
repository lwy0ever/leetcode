class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        cs = candidates
        cs.sort()
        
        n = len(cs)
        ans = []
        stack = []

        def dfs(cs,i,s):    # 之前已经累积了s,现在从cs[i]开始尝试
            if s == target:
                ans.append(stack.copy())
                return

            for j in range(i,n):
                if j > i and cs[j] == cs[j - 1]:    # 避免重复
                    continue
                if s + cs[j] > target:
                    break
                stack.append(cs[j])
                dfs(cs,j + 1,s + cs[j])
                stack.pop()
        dfs(cs,0,0)
        return ans