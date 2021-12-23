class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        pre = dict()    # pre[i] = n,表示i出现过,以其结尾的最大子序列长度为n
        for a in arr:
            pre[a] = max(pre.get(a,1),pre.get(a - difference,0) + 1)
        return max(pre.values())