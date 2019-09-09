class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ldeep = 0
        rdeep = 0
        stack = []
        ans = []
        for c in seq:
            if c == '(':
                if ldeep <= rdeep:
                    stack.append(0)
                    ans.append(0)
                    ldeep += 1
                else:
                    stack.append(1)
                    ans.append(1)
                    rdeep += 1
            else:
                pre = stack.pop()
                ans.append(pre)
                if pre == 0:
                    ldeep -= 1
                else:
                    rdeep -= 1
        return ans