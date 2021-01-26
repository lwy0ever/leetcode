class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = collections.Counter(arr)
        return len(cnt.keys()) == len(set(cnt.values()))