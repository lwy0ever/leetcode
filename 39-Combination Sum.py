class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
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
                if s + cs[j] > target:
                    break
                stack.append(cs[j])
                dfs(cs,j,s + cs[j])
                stack.pop()
        dfs(cs,0,0)
        return ans
        '''
        cs = candidates
        cs.sort()
        #print(cs)
        n = len(cs)
        ans = []
        valStack = []
        posStack = []
        s = 0
        p = 0
        while p < n:
            if s + cs[p] == target:
                s += cs[p]
                valStack.append(cs[p])
                posStack.append(p)
                ans.append(valStack.copy())
            elif s + cs[p] < target:
                valStack.append(cs[p])
                posStack.append(p)
                s += cs[p]
            else:
                if s == 0:
                    break
                s -= valStack.pop()
                p = posStack.pop() + 1
                while p == n and valStack:
                    s -= valStack.pop()
                    p = posStack.pop() + 1
            #print(valStack,posStack,s,p,ans)
        #print(ans)
        return ans
        '''