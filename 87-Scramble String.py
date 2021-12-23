class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def dfs(s1,s2):
            if s1 == s2:
                return True
            if collections.Counter(s1) != collections.Counter(s2):
                return False
            for i in range(1,len(s1)):
                if dfs(s1[:i],s2[:i]) and dfs(s1[i:],s2[i:]):
                    return True
                if dfs(s1[:i],s2[-i:]) and dfs(s1[i:],s2[:-i]):
                    return True
            return False
        
        return dfs(s1,s2)