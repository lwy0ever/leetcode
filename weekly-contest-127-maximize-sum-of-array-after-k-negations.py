class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # 找出负数,并排序
        # 同时绝对值最小的值:如果k > len(negative),则使用该值
        ans = sum(nums)
        n = len(nums)
        negative = []
        minABS = float('inf')
        for num in nums:
            if num < 0:
                negative.append(num)
            minABS = min(minABS,abs(num))
        #print(negative,minABS,k)
        if k >= len(negative):
            ans -= sum(negative) * 2
            k -= len(negative)
            if k & 1:
                ans -= minABS * 2
            return ans
        else:
            negative.sort()
            ans -= sum(negative[:k]) * 2
            return ans