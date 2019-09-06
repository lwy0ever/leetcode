class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        z = zip(*strs)
        ans = ''
        for cs in z:
            #print(cs)
            if len(set(cs)) == 1:
                ans += cs[0]
            else:
                break
        return ans