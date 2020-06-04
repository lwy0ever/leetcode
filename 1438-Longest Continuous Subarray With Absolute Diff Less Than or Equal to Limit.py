class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # 通过维护升序队列和降序队列,避免排序
        increaseStack = []  # 升序队列,记录值和nums[i]的下标.可能的最小值都在这个队列中
        decreaseStack = []  # 降序队列,记录值和nums[i]的下标.可能的最大值都在这个队列中
        indexI = 0  # 指向increaseStack
        indexD = 0  # 指向decreaseStack
        ans = 0
        l = 0   # l和r构成滑动窗口的两端
        for r,n in enumerate(nums):
            while len(increaseStack) > indexI and increaseStack[-1][0] > n:    # 将大值弹出,只关心小值
                increaseStack.pop()
            increaseStack.append((n,r))
            while len(decreaseStack) > indexD and decreaseStack[-1][0] < n:    # 将小值弹出,只关心大值
                decreaseStack.pop()
            decreaseStack.append((n,r))
            while indexI < len(increaseStack) and indexD < len(decreaseStack) and decreaseStack[indexD][0] - increaseStack[indexI][0] > limit:
                if increaseStack[indexI][1] <= l:
                    indexI += 1
                if decreaseStack[indexD][1] <= l:
                    indexD += 1
                l += 1
            ans = max(ans,r - l + 1)
            #print(increaseStack,indexI,decreaseStack,indexD,nums[l:r + 1])
        return ans
            