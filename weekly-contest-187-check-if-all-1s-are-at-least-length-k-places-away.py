class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        pre = float('-inf')
        for i,n in enumerate(nums):
            if n == 1:
                if i - pre - 1 < k:
                    return False
                pre = i
            #print(i,n,pre)
        return True