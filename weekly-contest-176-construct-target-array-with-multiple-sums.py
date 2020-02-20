class Solution:
    def isPossible(self, target: List[int]) -> bool:
        target.sort()
        s = sum(target)
        while target[-1] != 1:
            if target[-1] - (s - target[-1]) > 0:
                t = target.pop()
                bisect.insort(target,t - (s - t))
                s = s - t + (t - s + t)
            else:
                return False
            #print(target)
        return True