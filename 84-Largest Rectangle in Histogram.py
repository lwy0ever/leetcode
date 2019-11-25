class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 前一个0,可以让stack不会被弹空
        # 后一个0,可以保证全部有效数据都会被检查
        heights = [0] + heights + [0]
        stack = []  # 存储位置,形成一个递增序列
        ans = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                oldi = stack.pop()
                #print(stack[-1],i,ans)
                ans = max(ans,heights[oldi] * (i - 1 - stack[-1]))  # 位置i和位置stack[-1]不应该被包含
            stack.append(i)
            #print(stack,ans)
        return ans