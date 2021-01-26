class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        # 使用SortedList
        from sortedcontainers import SortedList
        # 先将奇数的num * 2,避免需要扩大的小数出现
        # 因为*2以后就是偶数,只能选择保持 or //2,所以只需要*2一次
        nums = SortedList(num << 1 if num & 1 else num for num in nums)
        # 排序后的nums,如果nums[-1]是偶数,则nums[-1]//2可能使结果更小
        ans = nums[-1] - nums[0]
        while nums[-1] & 1 == 0:
            nums.add(nums.pop() >> 1)
            ans = min(ans,nums[-1] - nums[0])
        #print(nums)
        return ans