class Solution:
    def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        ans = []
        n = len(increase)
        c,r,h = [0],[0],[0] # 记录每天的c\r\h值
        for ic,ir,ih in increase:
            c.append(c[-1] + ic)
            r.append(r[-1] + ir)
            h.append(h[-1] + ih)
        for rc,rr,rh in requirements:
            posc = bisect.bisect_left(c,rc)
            posr = bisect.bisect_left(r,rr)
            posh = bisect.bisect_left(h,rh)
            pos = max(posc,posr,posh)
            if pos == n + 1:
                ans.append(-1)
            else:
                ans.append(pos)
        return ans