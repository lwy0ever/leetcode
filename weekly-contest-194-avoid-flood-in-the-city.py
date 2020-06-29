class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        cache = []  # 存放可以抽水的坐标
        stat = dict()  # 记录当前湖泊的状态:不存在表示湖泊为空,否则表示湖泊变满的日子
        for i in range(n):
            #print(i,stat)
            #print(cache)
            if rains[i] == 0:
                cache.append(i)
            else:   # 下雨
                if rains[i] in stat:
                    if cache:
                        for j in range(len(cache)):
                            day = cache[j]
                            if day > stat[rains[i]]:
                                ans[day] = rains[i]
                                stat[rains[i]] = i
                                cache.pop(j)
                                break
                        else:
                            return []
                    else:
                        return []
                else:
                    stat[rains[i]] = i
        while cache:
            day = cache.pop()
            ans[day] = 1
        return ans