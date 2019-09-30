class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = collections.Counter(arr)
        ctt = collections.Counter(cnt.values())
        #print(ctt.most_common(1)[0][1])
        return ctt.most_common(1)[0][1] == 1
        