class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a1 = version1.split('.')
        n1 = len(a1)
        a2 = version2.split('.')
        n2 = len(a2)
        i = 0
        while i < n1 or i < n2:
            if i < n1:
                t1 = int(a1[i])
            else:
                t1 = 0
            if i < n2:
                t2 = int(a2[i])
            else:
                t2 = 0
            if t1 > t2:
                return 1
            elif t1 < t2:
                return -1
            i += 1
        return 0