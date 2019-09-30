class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        popind = 0
        m = len(popped)
        for ps in pushed:
            stack.append(ps)
            while stack and popind < m and stack[-1] == popped[popind]:
                stack.pop()
                popind += 1
        return popind == m
        '''
        stack = []
        popind = 0
        n = len(pushed)
        m = len(popped)
        if m == 0:
            return True
        stack.append(pushed[0])
        pushind = 1
        while popind < m:
            #print(stack,pushind,popind)
            #print(pushed[pushind])
            if stack:
                if popind < m:
                    if stack[-1] == popped[popind]:
                        stack.pop()
                        popind += 1
                        continue
            if pushind == n:
                break
            stack.append(pushed[pushind])
            pushind += 1
        return popind == m
        '''