class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        ans = []
        S += 'X'
        n = len(S)
        pre = ''
        cnt = 1
        start = -1
        for i in range(n):
            if S[i] != pre:
                #print(S[i],cnt)
                if cnt >= 3:
                    ans.append([start,i - 1])
                pre = S[i]
                start = i
                cnt = 1
            else:
                cnt += 1
        return ans
            