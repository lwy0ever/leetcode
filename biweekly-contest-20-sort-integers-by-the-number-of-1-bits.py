class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count1(n):
            ans = 0
            while n:
                n &= (n - 1)
                ans += 1
            return ans
        
        return sorted(arr,key = lambda x:(count1(x),x))