class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ans = [[0,0]]   # 省掉判断ans为空
        loc = [] # 用于存储building的Li,Ri和Hi
        for l,r,h in buildings:
            loc.append([l,-h])    # Li的高度设置为-h,从而保证排序的时候,同等高度,Li在Ri的左侧
            loc.append([r,h])
        loc.sort()
        #print(loc)

        height = [0] # 存储当前的建筑高度负数,排序的(由于是负数,所以最高的在最左侧)
        for i,h in loc:
            if h < 0:   # 说明是左边
                bisect.insort(height,h)
            else:
                toRemove = bisect.bisect(height,-h)
                height.pop(toRemove - 1)
            highest = -height[0]    # 当前最高
            if ans[-1][1] != highest:
                ans.append([i,highest])
        return ans[1:]