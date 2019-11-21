class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        # 由于nums[0],nums[1]一定会保留
        if n <= 2:
            return n
        # 需要从nums[1]开始,因为需要统计重复次数
        l = 1   # 记录有效的列表长度,nums[:l]已经完成去重要求
        r = 1   # 查找的位置
        repeatNum = 1
        while r < n:
            #print(l,r,nums[l - 1],nums[r],repeatNum)
            if nums[r] == nums[l - 1]:
                if repeatNum == 1:
                    repeatNum += 1
                    nums[l] = nums[r]
                    l += 1
            else:
                repeatNum = 1
                nums[l] = nums[r]
                l += 1
            r += 1
        return l
                    