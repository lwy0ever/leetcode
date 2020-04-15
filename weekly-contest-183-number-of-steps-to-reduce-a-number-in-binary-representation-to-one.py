class Solution:
    def numSteps(self, s: str) -> int:
        arr = []
        for c in s:
            arr.append(c)
        ans = 0
        while len(arr) > 1: # 由于s[0] == '1',所以不存在s = '0'的情况
            if arr[-1] == '0':
                arr.pop()
            else:
                i = len(arr) - 1
                while arr[i] == '1' and i >= 0:
                    arr[i] = '0'
                    i -= 1
                if i >= 0:
                    arr[i] = '1'
                else:
                    arr.insert(0,'1')
            ans += 1
        return ans