class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        
        def c(n):
            if n == 1:
                return 0
            if n ** 0.5 == int(n ** 0.5):
                return 0
            ans = 1 + n
            cnt = 2
            for i in range(2,int(n ** 0.5) + 1):
                if n % i == 0:
                    cnt += 2
                    if cnt > 4:
                        return 0
                    ans += i + n // i
            return ans if cnt == 4 else 0

        for n in nums:
            ans += c(n)
            #print(ans)
        return ans