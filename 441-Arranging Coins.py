class Solution:
    def arrangeCoins(self, n: int) -> int:
        # k row need :k * (1 + k) / 2
        # so n >= k * (1 + k) / 2
        # --> k * (1 + k) <= n * 2
        # so k <= (n * 2) ** 0.5
        ans = int((n * 2) ** 0.5)
        while ans * (ans + 1) > n * 2:
            #print('xxx')
            ans -= 1
        return ans
    
        #return int((1 / 4 + n * 2) ** 0.5 - 1 / 2)