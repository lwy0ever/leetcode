class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        zero = 0
        for x in arr:
            if x == 0:
                if zero == 1:
                    return True
                else:
                    zero = 1
        s = set(arr)
        s.discard(0)
        for x in s:
            if (x * 2) in s or (x & 1 == 0 and (x // 2) in s):
                #print(x)
                return True
        return False
                