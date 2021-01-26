class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        nums.sort()
        if nums[0] >= n:
            return n
        i = 1
        while i < n:
            if nums[i] != nums[i - 1]:
                x = n - i
                #print(i,x)
                if nums[i] >= x and nums[i - 1] < x:
                    return x
            i += 1
        return -1