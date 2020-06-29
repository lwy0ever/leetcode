class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = collections.Counter(arr)
        val = []
        for v in cnt.values():
            val.append(v)
        val.sort(reverse = True)
        while k > 0:
            if val[-1] > k:
                return len(val)
            elif val[-1] == k:
                return len(val) - 1
            else:
                k -= val[-1]
                val.pop()
        return len(val)