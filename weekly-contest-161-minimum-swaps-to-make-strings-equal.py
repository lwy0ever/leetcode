class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        cnt1 = [0,0]
        cnt2 = [0,0]
        n = len(s1)
        for i in range(n):
            if s1[i] == s2[i]:
                continue
            if s1[i] == 'x':
                cnt1[0] += 1
                cnt2[1] += 1
            else:
                cnt1[1] += 1
                cnt2[0] += 1
        #print(cnt1)
        #print(cnt2)
        # xy互换
        ans = 0
        while cnt1[0] >= 2 and cnt2[1] >= 2:
            cnt1[0] -= 2
            cnt2[1] -= 2
            ans += 1
        while cnt1[1] >= 2 and cnt2[0] >= 2:
            cnt1[1] -= 2
            cnt2[0] -= 2
            ans += 1
        #print(cnt1)
        #print(cnt2)
        while cnt1[0] >= 1 and cnt1[1] >= 1 and cnt2[0] >= 1 and cnt2[1] >= 1:
            cnt1[0] -= 1
            cnt1[1] -= 1
            cnt2[0] -= 1
            cnt2[1] -= 1
            ans += 2
        if cnt1[1] == 0 and cnt2[0] == 0 and cnt1[0] == 0 and cnt2[1] == 0:
            return ans
        return -1
