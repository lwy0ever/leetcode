class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 考虑nums[i],i > k
        # 在nums[i - k:i]中,所有比nums[i]小的数都将不起作用,可以弹出
        # 此时nums[i]是最小的,放在队列最左侧
        def clearStack(i):  # 将deque中小于nums[i]的弹出
            # 如果i - k是当前最大值,则需要弹出
            # 否则,无需理会
            # 那么,会不会有i < j,nums[stack[i]] > nums[stack[j]],stack[i]先被弹出,而stack[j]无法被弹出的情况呢?
            # 假设stack[j] < stack[i],由于nums[stack[i]] > nums[stack[j]]
            # 在扫描stack[0]的时候,先扫描到i,j没有被扫描到
            # 但是由于nums[stack[i]] > nums[stack[j]],在stack[i]被插入的时候,stack[j]已经被弹出了
            if stack and stack[0] == i - k:
                stack.pop(0)
            while stack and nums[i] > nums[stack[-1]]:
                stack.pop()
            #print(stack)

        stack = []  # 存放nums的下标,按照nums[i]从大到小排序
        n = len(nums)
        maxIndex = 0
        ans = []
        for i in range(n):
            clearStack(i)
            stack.append(i)
            #print(stack)
            if i >= k - 1:
                ans.append(nums[stack[0]])
        return ans