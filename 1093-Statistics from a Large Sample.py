class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        l = 0
        r = len(count) - 1

        minimum = float('inf')
        maximum = float('-inf')
        if count[l] > 0:
            minimum = min(minimum,l)
            maximum = max(maximum,l)
        if count[r] > 0:
            minimum = min(minimum,r)
            maximum = max(maximum,r)
        s = count[l] * l + count[r] * r
        cntL = count[l]
        cntR = count[r]
        maxcnt = 0  # 众数计数
        mode = 0    # 众数值
        if count[l] > count[r]:
            mode = l
            maxcnt = count[l]
        else:
            mode = r
            maxcnt = count[r]
        # 两侧逼近求中位数
        while l < r:
            #print(l,r)
            if cntL <= cntR:
                t = l + 1
                while count[t] == 0:
                    #print(l,t)
                    t += 1
                l = t
                if l == r:
                    break
                cntL += count[l]
            else:
                t = r - 1
                while count[t] == 0:
                    #print(r,t)
                    t -= 1
                r = t
                if l == r:
                    break
                cntR += count[r]
            if cntL > cntR:
                median = l
            elif cntL < cntR:
                median = r
            else:
                median = (l + r) / 2
            minimum = min(minimum,t)
            maximum = max(maximum,t)
            s += count[t] * t
            if count[t] > maxcnt:
                mode = t
                maxcnt = count[t]
        #print(s,cntL,cntR)
        return minimum,maximum,s / (cntL + cntR),median,mode