class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        if ladders >= n - 1:
            return n - 1
        needBricks = []
        for i in range(n - 1):
            # 向下,不需要brick和ladder
            if heights[i] >= heights[i + 1]:
                continue
            needed = heights[i + 1] - heights[i]
            m = len(needBricks)
            # ladder足够多,默认用ladder
            if m < ladders:
                bisect.insort(needBricks,needed)
                continue
            p = bisect.bisect_right(needBricks,needed)
            bisect.insort(needBricks,needed)
            #print(i,needBricks,needed,bricks,p)
            # needBricks左半区为brick方案,右半区为ladder方案
            if p <= m - ladders:    # 新需求在brick区
                if bricks >= needed:    # brick足够
                    bricks -= needed
                else:
                    return i
            else:   # 新需求在ladder区
                if bricks >= needBricks[m - ladders]:    # ladder区的第一个元素移入brick区
                    bricks -= needBricks[m - ladders]
                else:
                    return i
        return i + 1