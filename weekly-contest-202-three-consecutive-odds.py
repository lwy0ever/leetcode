class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0
        for a in arr:
            if a & 1:
                cnt += 1
                if cnt >= 3:
                    return True
            else:
                cnt = 0
        return False