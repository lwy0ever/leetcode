class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        l = len(nums)
        # d[i]表示i出现的次数
        d = collections.defaultdict(int)
        # freq[i]表示出现次数为i的元素个数
        freq = collections.defaultdict(int)
        maxFreq = 0
        ans = 0
        for i,n in enumerate(nums):
            if freq[d[n]] > 0:
                freq[d[n]] -= 1
            d[n] += 1
            freq[d[n]] += 1
            maxFreq = max(maxFreq,d[n])
            # 只有一个元素出现maxFreq次,其余元素都出现maxFreq - 1次(也就是freq[maxFreq - 1] * (maxFreq - 1) + freq[maxFreq] * maxFreq == i + 1)
            #print(freq[maxFreq],freq[maxFreq - 1] * (maxFreq - 1) + freq[maxFreq] * maxFreq,i + 1)
            if freq[maxFreq] == 1 and freq[maxFreq - 1] * (maxFreq - 1) + freq[maxFreq] * maxFreq == i + 1:
                ans = i + 1
            # 或者 只有一个元素出现1次,其余元素都出现maxFreq次
            if freq[1] == 1 and freq[maxFreq] * maxFreq + 1 == i + 1:
                ans = i + 1
            # 或者 所有元素都出现maxFreq次
            if maxFreq == 1:
                ans = i + 1
            #print(n,d,freq,maxFreq)
        return ans