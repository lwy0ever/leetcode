class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = collections.Counter(arr)
        for k in sorted(cnt.keys(),reverse = True):
            if k == cnt[k]:
                return k
        return -1