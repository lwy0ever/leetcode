class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        cache = {}
        locStart = locations[start]
        locFinish = locations[finish]
        n = len(locations)
        locations.sort()
        locIndex = {loc:i for i,loc in enumerate(locations)}
        indexStart = locIndex[locStart]
        indexFinish = locIndex[locFinish]
        #print(indexStart,indexFinish)
        #print(locIndex)
        def cr(pos,f):  # 在位置locations[pos](其中locations已经排序),有f油的情况下,到达locFinish的方法数
            if (pos,f) in cache:
                return cache[(pos,f)]
            if f < 0:
                return 0
            ans = 0
            if pos == indexFinish:   # 已经到达,可以不再继续
                ans += 1
            # 由于locations已经排序,从pos分别向左/向右
            p = pos - 1
            while p >= 0:
                dis = abs(locations[p] - locations[pos])
                if dis <= f:
                    ans += cr(p,f - dis)
                else:
                    break
                p -= 1
            p = pos + 1
            while p < n:
                dis = abs(locations[p] - locations[pos])
                if dis <= f:
                    ans += cr(p,f - dis)
                else:
                    break
                p += 1
            cache[(pos,f)] = ans
            #print(cache)
            return ans
        return cr(indexStart,fuel) % (10 ** 9 + 7)
        '''
        cache = {}
        def cr(loc,f):  # 在位置loc,有f油的情况下,到达finish的方法数
            if (loc,f) in cache:
                return cache[(loc,f)]
            if f < 0:
                return 0
            ans = 0
            if loc == locations[finish]:   # 已经到达,可以不再继续
                ans += 1
            for l in locations: # 由于locations各不相同,不用关心下标
                if l == loc:    # 不能从自身到自身
                    continue
                if abs(loc - l) <= f:
                    ans += cr(l,f - abs(loc - l))
            cache[(loc,f)] = ans
            return ans
        return cr(locations[start],fuel) % (10 ** 9 + 7)
        '''