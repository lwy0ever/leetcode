class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # 方法1:单调栈
        # 时间复杂度O(n)
        # 空间复杂度O(n)
        # 定义,当nums[i] = nums[j]时,如果i < j,则称nums[i] < nums[j]
        # 站在点i
        # 如果左侧比nums[i]小的点在m点
        # 如果右侧比nums[i]小的点在n点
        # 那么以nums[i]为最小点的子数组数量为(n - i) * (i - m)
        # 定义minLeft[i] = m,minRight[i] = n
        # 左侧比nums[i]大的点为maxLeft[i]
        # 右侧比nums[i]大的点为maxRight[i]
        # minLeft,minRight,maxLeft,maxRight可以利用单调栈获得
        n = len(nums)
        minLeft = [0] * n
        maxLeft = [0] * n
        minStack = []   # nums[minStack[i]]是递增的
        maxStack = []   # nums[maxStack[i]]是递减的
        for i,num in enumerate(nums):
            while minStack and nums[minStack[-1]] > num:
                minStack.pop()
            minLeft[i] = minStack[-1] if minStack else -1
            minStack.append(i)

            # 如果 nums[maxStack[-1]] == num, 那么根据定义，
            # nums[maxStack[-1]] 逻辑上小于 num，因为 maxStack[-1] < i
            while maxStack and nums[maxStack[-1]] <= num:
                maxStack.pop()
            maxLeft[i] = maxStack[-1] if maxStack else -1
            maxStack.append(i)

        minRight = [0] * n
        maxRight = [0] * n
        minStack = []   # nums[minStack[i]]是递增的
        maxStack = []   # nums[maxStack[i]]是递减的
        for i in range(n - 1,-1,-1):
            num = nums[i]
            # 如果 nums[minStack[-1]] == num, 那么根据定义，
            # nums[minStack[-1]] 逻辑上大于 num，因为 minStack[-1] > i
            while minStack and nums[minStack[-1]] >= num:
                minStack.pop()
            minRight[i] = minStack[-1] if minStack else n
            minStack.append(i)

            while maxStack and nums[maxStack[-1]] < num:
                maxStack.pop()
            maxRight[i] = maxStack[-1] if maxStack else n
            maxStack.append(i)
            
        sumMax = 0
        sumMin = 0
        for i in range(n):
            sumMax += nums[i] * (maxRight[i] - i) * (i - maxLeft[i])
            sumMin += nums[i] * (minRight[i] - i) * (i - minLeft[i])
        return sumMax - sumMin

        
        # 方法2:遍历
        # 时间复杂度O(n ^ 2)
        # 空间复杂度O(1)
        n = len(nums)
        ans = 0
        for i in range(n - 1):
            mi = nums[i]
            ma = nums[i]
            for j in range(i + 1,n):
                mi = min(mi,nums[j])
                ma = max(ma,nums[j])
                ans += ma - mi
        return ans