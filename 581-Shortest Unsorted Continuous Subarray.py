class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # method 1:
        # O(N)复杂度算法
        n = len(nums)
        # 如果区间[left,right]需要排序
        # 则left左侧都是排序好的,right右侧都是排序好的
        # 从左向右寻找出现逆序的位置
        maxN = float('-inf')    # 已出现的最大值
        right = -1
        for i in range(n):
            if maxN > nums[i]:  # 有逆序,左侧区间需要排序
                right = i
            else:
                maxN = nums[i]

        # 从右向左寻找出现逆序的位置
        minN = float('inf')    # 已出现的最小值
        left = -1
        for i in range(n - 1,-1,-1):
            if minN < nums[i]:  # 有逆序,右侧区间需要排序
                left = i
            else:
                minN = nums[i]

        return right - left + 1 if right != -1 else 0

        # method 2:
        # O(NlogN)复杂度算法
        # 排序
        # 从左往右和nums对比,如果出现不一样的,则说明右侧需要排序
        # 从右往左和nums对比,如果出现不一样的,则说明左侧需要排序
        n = len(nums)
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                break
        else:   # 所有的nums[i] <= nums[i + 1],说明没有倒序
            return 0
        
        sortedNums = sorted(nums)
        left = 0
        for i in range(n):
            if sortedNums[i] != nums[i]:
                left = i
                break

        right = n
        for i in range(n - 1,-1,-1):
            if sortedNums[i] != nums[i]:
                right = i
                break
        
        return right - left + 1