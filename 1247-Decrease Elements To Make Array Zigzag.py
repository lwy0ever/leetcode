class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        a1 = 0
        a2 = 0
        if n % 2 == 0:
            for i in range(1,n - 1,2):
                mi = min(nums[i - 1],nums[i + 1])
                if nums[i] >= mi:
                    a1 += nums[i] - mi + 1
            mi = nums[n - 2]
            if nums[n - 1] >= mi:
                a1 += nums[n - 1] - mi + 1
            mi = nums[1]
            if nums[0] >= mi:
                a2 += nums[0] - mi + 1
            for i in range(2,n,2):
                mi = min(nums[i - 1],nums[i + 1])
                if nums[i] >= mi:
                    a2 += nums[i] - mi + 1
            return min(a1,a2)
        else:
            for i in range(1,n - 1,2):
                mi = min(nums[i - 1],nums[i + 1])
                if nums[i] >= mi:
                    a1 += nums[i] - mi + 1
            mi = nums[1]
            if nums[0] >= mi:
                a2 += nums[0] - mi + 1
            for i in range(2,n - 1,2):
                mi = min(nums[i - 1],nums[i + 1])
                if nums[i] >= mi:
                    a2 += nums[i] - mi + 1
            mi = nums[n - 2]
            if nums[n - 1] >= mi:
                a2 += nums[n - 1] - mi + 1
            return min(a1,a2)
