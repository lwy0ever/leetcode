class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = max(sum(nums) // threshold,1)
        r = 0
        t = threshold // len(nums)
        for n in nums:
            r += math.ceil(n / t)
        while l < r:
            #print(l,r)
            m = (l + r) // 2
            s = 0
            for n in nums:
                s += math.ceil(n / m)
            #print(s,m)
            if s > threshold:
                l = m + 1
            else:
                r = m
        return l