class Solution:
    def countSegments(self, s: str) -> int:
        ans = 0
        isPreBlank = True
        for c in s:
            if c != ' ':
                if isPreBlank:
                    ans += 1
                isPreBlank = False
            else:
                isPreBlank = True
        return ans
        '''
        return len(s.split())
        '''