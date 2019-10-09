class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        d = {}
        for a in arr:
            if a - difference in d:
                d[a] = max(d.get(a,0),d[a - difference] + 1)
            else:
                d[a] = 1
        return max(d.values())