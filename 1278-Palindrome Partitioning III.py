class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        rDic = {}
        tochangeDic = {}
        def tochange(s):
            if s in tochangeDic:
                return tochangeDic[s]
            n = len(s)
            if n <= 1:
                #print('toc',s,0)
                return 0
            ans = 0
            for i in range(n // 2):
                if s[i] != s[-i-1]:
                    ans += 1
            #print('toc',s,ans)
            tochangeDic[s] = ans
            return ans

        def r(s,k):
            nonlocal rDic
            if (s,k) in rDic:
                return rDic[(s,k)]
            n = len(s)
            if k == 1:
                return tochange(s)
            if n == k:
                return 0
            ans = float('inf')
            for i in range(1,n - k + 2):
                ans = min(ans,tochange(s[:i]) + r(s[i:],k - 1))
                #print(s,i,s[:i],s[i:],ans)
            rDic[(s,k)] = ans
            return ans
        
        return r(s,k)