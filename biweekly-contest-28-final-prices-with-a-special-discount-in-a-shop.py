class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        stack = []
        for p in prices[::-1]:
            last = 0
            while stack and p < stack[-1]:
                stack.pop()
            if stack:
                ans.append(p - stack[-1])
            else:
                ans.append(p)
            stack.append(p)
        return ans[::-1]
