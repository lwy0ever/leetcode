class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # 优化求和方式
        ans = 0
        stack = dict()
        for a,b in dominoes:
            if a > b:
                a,b = b,a
            if (a,b) in stack:
                ans += stack[(a,b)]
                stack[(a,b)] += 1
            else:
                stack[(a,b)] = 1
        return ans

        '''
        stack = dict()
        for a,b in dominoes:
            if a > b:
                a,b = b,a
            if (a,b) in stack:
                stack[(a,b)] += 1
            else:
                stack[(a,b)] = 1
        ans = 0
        for v in stack.values():
            ans += v * (v - 1) // 2
        return ans
        '''