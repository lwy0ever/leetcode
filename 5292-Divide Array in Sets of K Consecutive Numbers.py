class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        l = len(nums)
        if k == 1:
            return True
        if l % k != 0:
            return False
        d = collections.Counter(nums)
        # print(d)
        ks = sorted(d.keys())
        for key in ks:
            while d[key] != 0:
                for i in range(k):
                    if d[key + i] == 0:
                        return False
                    d[key + i] -= 1
        return True