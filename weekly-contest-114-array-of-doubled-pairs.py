class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        cnt = collections.Counter(arr)
        arr.sort(key = lambda x:abs(x))
        for a in arr:
            if cnt[a] > 0:
                if cnt[a * 2] > 0:
                    cnt[a] -= 1
                    cnt[a * 2] -= 1
                else:
                    return False
        return True