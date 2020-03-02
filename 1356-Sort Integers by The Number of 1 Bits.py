class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def c(n):
            ans = 0
            while n > 0:
                n &= (n - 1)
                ans += 1
            return ans
        
        return sorted(arr,key = lambda x:(c(x),x))