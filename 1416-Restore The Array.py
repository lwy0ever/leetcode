class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        # 对于每一个字符i，它的可能性由几部分相加而得：
        # 当它这个字符自己组成一个数的时候，可能性等于dp[i-1]
        # 当它和它前边1个字符组成一个数的时候，可能性等于dp[i-2]
        # ...等等
        # 当它与它前边n个字符组成一个数的时候（这个数小于等于k），可能性为dp[i-n]
        # 所以可以从第一个字符向后逐渐求得第n个字符的可能性个数dp[len(s)]，也就是长度为len(s)的字符串的回复数组的可能个数
        n = len(s)
        dp = [0] * (n + 1) # dp[i]表示s[:i]的方案数
        dp[0] = 1   # 相当于s = ''
        for i in range(1,n + 1):
            for j in range(i - 1,-1,-1):
                if s[j] == '0':
                    continue
                if int(s[j:i]) <= k:
                    dp[i] += dp[j]
                else:
                    if s[i - 1] == '0' and dp[i] == 0:  # 如果当前字符是0,且与前面的第一个非0字符构成的数字大于k,那么说明往后不能再构成数字了,直接返回0
                        return 0
                    break
            dp[i] %= 10 ** 9 + 7
        return dp[-1]