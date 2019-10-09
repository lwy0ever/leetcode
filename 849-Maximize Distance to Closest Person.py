class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ans = 1
        pre = -1    # 前一个1出现的位置
        for i,s in enumerate(seats):
            if s == 1:
                if pre == -1:
                    ans = max(ans,i - 0)
                else:
                    ans = max(ans,(i - pre) // 2)
                pre = i
        if s == 0:  # 如果最后一个是0,那么之前一定出现过1,所以pre不会是-1
            ans = max(ans,i - pre)
        return ans