class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        # 计算每一位出现1的次数
        # 那么len-次数=0出现的次数
        # 相乘,再求和,就是汉明距离和
        l, d = len(nums), collections.defaultdict(int)
        for n in nums:
            while n:
                d[n ^ n & (n - 1)] += 1
                n &= n - 1
        return sum(c * (l - c) for _, c in d.items())
        '''
        ans = 0
        n = len(nums)
        isAllZero = False
        while not isAllZero:
            isAllZero = True
            ones = 0
            for i in range(n):
                if nums[i] & 1: #nums[i] & 1 == 1
                    ones += 1
                nums[i] >>= 1
                if nums[i] > 0:
                    isAllZero = False
            ans += (n - ones) * ones
        return ans
        '''
        '''
        def cnt(x):
            r = 0
            while x > 0:
                x = x & (x - 1)
                r += 1
            return r

        ans = 0
        for a,b in itertools.combinations(nums, 2):
            #print(a,b)
            ans += cnt(a ^ b)
        return ans
        '''
