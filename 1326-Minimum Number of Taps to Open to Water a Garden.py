class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        area = []   # area[i] = (from,to)表示水龙头i的覆盖范围是[from,to]
        for i in range(n + 1):
            area.append([i - ranges[i],i + ranges[i]])
        area.sort(key = lambda x:(x[0],-x[1]))
        #print(area)
        ans = 0
        _max = -1   # 灌溉的最远范围
        i = 0   # 灌溉到的水龙头位置
        cur = 0 # area的指针
        while i <= n:
            #print('i:',i)
            #toadd = False
            while cur <= n and i >= area[cur][0]:   # 找到所有能覆盖到i的范围的水龙头
                if area[cur][1] > _max:
                    _max = area[cur][1] # 获取最远灌溉范围
                #print(cur,i,area[cur],_max,ans)
                cur += 1
            ans += 1    # 需要数量+1
            if _max >= n:   # 已经全覆盖,返回结果
                return ans
            if _max < i + 1:    # 没有找到能覆盖到i + 1的水龙头,说明中断了
                return -1
            i = _max    # 更新最远范围
        return ans