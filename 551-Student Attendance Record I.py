class Solution:
    def checkRecord(self, s: str) -> bool:
        cntA = 0
        cntL = 0
        for c in s:
            if c == 'A':
                cntA += 1
                if cntA > 1:
                    return False
                cntL = 0
            elif c == 'L':
                cntL += 1
                if cntL >= 3:
                    return False
            else:
                cntL = 0
        return True