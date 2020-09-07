class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        leftIndex = 0
        rightIndex = n - 1
        leftMax = height[leftIndex]
        rightMax = height[rightIndex]

        ans = 0
        while leftIndex < rightIndex:
            #print(leftIndex,rightIndex,leftMax,rightMax)
            if leftMax <= rightMax: # 对短边进行结算
                ans += leftMax - height[leftIndex]  # 低于最高短边的,可以储水
                leftIndex += 1
                leftMax = max(leftMax,height[leftIndex])    # 更新短边
            else:
                ans += rightMax - height[rightIndex]
                rightIndex -= 1
                rightMax = max(rightMax,height[rightIndex])
        #print(leftIndex,rightIndex,leftMax,rightMax)
        return ans