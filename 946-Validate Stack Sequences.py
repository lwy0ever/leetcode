class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        idx = 0
        stack = list()
        for push in pushed:
            stack.append(push)
            while idx < n and stack and stack[-1] == popped[idx]:
                stack.pop()
                idx += 1
        return idx == n
