class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        length = len(strs[0])
        for i in range(length):
            for s in strs[1:]:
                if i >= len(s) or s[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]