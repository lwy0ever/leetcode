class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        ans = 0
        n = len(light)
        dp = [0] * (n + 1)
        dp[0] = 2
        _max = 0
        for l in light:
            _max = max(_max,l)
            if dp[l - 1] == 2:
                dp[l] = 2
                for i in range(l + 1,_max + 1):
                    if dp[i] == 1:
                        dp[i] = 2
                    else:
                        break
                if dp[_max] == 2:
                    ans += 1
            else:
                dp[l] = 1
        return ans