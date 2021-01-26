class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        cnt = 0
        pre = ''
        prePos = -1
        ans = []
        for i,c in enumerate(s):
            if c == pre:
                cnt += 1
            else:
                if cnt >= 3:
                    ans.append([prePos,i - 1])
                cnt = 1
                pre = c
                prePos = i
        if cnt >= 3:
            ans.append([prePos,i])
        return ans