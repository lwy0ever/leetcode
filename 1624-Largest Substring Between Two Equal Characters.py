class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        _min = [-1] * 26
        _max = [-1] * 26
        for i,c in enumerate(s):
            p = ord(c) - ord('a')
            if _min[p] == -1:
                _min[p] = i
                _max[p] = i
            else:
                _max[p] = i
        ans = -1
        for i in range(26):
            ans = max(ans,_max[i] - _min[i] - 1)
        return ans