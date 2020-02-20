class Solution:
    def lengthLongestPath(self, input: str) -> int:
        arr = input.split('\n')
        ans = 0
        stack = []  # 相比下面的解法,stack不再记录具体的path,只记录path的长度
        for a in arr:
            t = a.split('\t')
            n = len(t)
            stack = stack[:n - 1] + [len(t[-1])]
            if '.' in t[-1]:
                ans = max(ans,sum(stack) + len(stack) - 1)
        return ans
        '''
        arr = input.split('\n')
        ans = 0
        stack = []
        for a in arr:
            t = a.split('\t')
            n = len(t)
            stack = stack[:n - 1] + [t[-1]]
            if '.' in t[-1]:
                ans = max(ans,len('/'.join(stack)))
        return ans
        '''