from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt1 = Counter(s1)
        n = len(s2)
        ll = 0
        for i in range(n):
            if cnt1[s2[i]] > 0:
                cnt1[s2[i]] -= 1
            elif s2[i] in cnt1:
                while cnt1[s2[i]] == 0:
                    cnt1[s2[ll]] += 1
                    ll += 1
                    #print(ll,cnt1)
                cnt1[s2[i]] -= 1
            else:
                cnt1 = Counter(s1)
                ll = i + 1
            #print(s2[i],ll,cnt1)
            if len(+cnt1) == 0:
                return True
        return False
            
                