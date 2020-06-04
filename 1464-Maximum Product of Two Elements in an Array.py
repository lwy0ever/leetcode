class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ma = 0
        mb = 0
        for n in nums:
            if n > mb:
                if n >= ma:
                    mb = ma
                    ma = n
                else:
                    mb = n
        return (ma - 1) * (mb - 1)