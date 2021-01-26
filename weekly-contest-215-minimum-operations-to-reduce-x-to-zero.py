class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # 双指针
        # 将数组分成3份,第1份+第3份=x,并且需要第1,3份的长度最短
        ans = float('inf')
        s = sum(nums)
        n = len(nums)
        target = s - x
        #print(target)
        if target < 0:
            return -1
        if target == 0:
            return n
        l = 0
        r = 0
        mid = 0
        while r < n:
            if mid < target:
                mid += nums[r]
                r += 1
            elif mid > target:
                mid -= nums[l]
                l += 1
            else:   # mid == target
                mid = mid - nums[l] + nums[r]
                l += 1
                r += 1
            if mid == target:
                ans = min(ans,l + (n - r))
        return -1 if ans == float('inf') else ans