class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        # 剩余字符串的起始位置为i,之前已经产生过的字符串存放在集合pre里
        def g(ind,pre):
            if ind == n:
                return 0
            ans = float('-inf')
            for end in range(ind + 1,n + 1):
                if s[ind:end] not in pre:
                    pre.add(s[ind:end])
                    ans = max(ans,1 + g(end,pre))
                    pre.remove(s[ind:end])
            #print(ind,pre,ans)
            return ans
        return g(0,set())
            