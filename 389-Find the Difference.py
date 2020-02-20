class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # 异或法
        ans = ord(t[0])
        for c in s:
            ans ^= ord(c)
        for c in t[1:]:
            ans ^= ord(c)
        return chr(ans)
        '''
        return list((collections.Counter(t) - collections.Counter(s)).keys())[0]
        '''