class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if s == '':
            return []
        
        ans = []
        def part(arr,s):
            if s == '':
                nonlocal ans
                ans.append(arr)
                return
            n = len(s)
            for i in range(1,n + 1):
                w = s[:i]
                if w == w[::-1]:
                    part(arr + [w],s[i:])
        
        part([],s)
        return ans
            