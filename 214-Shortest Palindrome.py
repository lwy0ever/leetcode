class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # KMP算法
        n = len(s)
        newS = s + '#' + s[::-1]
        newN = len(newS)
        table = [0] * newN # KMP映射表
        for i in range(1,newN):
            t = table[i - 1]
            while t > 0 and newS[i] != newS[t]:
                t = table[t - 1]
            if newS[i] == newS[t]:
                t += 1
            table[i] = t
        #print(s,n,newS,newN)
        #print(table)
        return s[::-1][:n - table[newN - 1]] + s

        '''
        n = len(s)
        l = 0
        # 通过查找肯定非回文的长度,减小需要检查的长度
        for r in range(n - 1,-1,-1):
            if s[l] == s[r]:
                l += 1
        if l == n:
            return s
        return s[l:][::-1] + self.shortestPalindrome(s[:l]) + s[l:]
        '''