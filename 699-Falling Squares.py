class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        # pos和height是等长的数组,pos[i]表示从坐标i开始,高度是height[i]
        pos = []
        height = []
        # 初始化
        pos.append(0)
        height.append(0)
        ans = []
        for left,side in positions:
            right = left + side - 1
            # leftIndex使用bisect_right,为了忽略pos[i] == pos[i + 1]这种情况
            leftIndex = bisect.bisect_right(pos,left)
            rightIndex = bisect.bisect_right(pos,right)
            # 新的square可能打断了之前的一个连续区间,需要找到这个区间的高度,补在新的square后面
            lastHeight = height[rightIndex - 1]
            # 找到新square覆盖区域的最大高度
            maxHeight = max(height[max(0,leftIndex - 1):rightIndex])
            # 删掉被覆盖的区间
            pos = pos[:leftIndex] + pos[rightIndex:]
            height = height[:leftIndex] + height[rightIndex:]
            # 补充新square后面的区间
            pos.insert(leftIndex,right + 1)
            height.insert(leftIndex,lastHeight)
            # 新square区间
            pos.insert(leftIndex,left)
            height.insert(leftIndex,maxHeight + side)
            ans.append(max(maxHeight + side,ans[-1] if ans else 0))
        return ans
