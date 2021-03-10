class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        #print(slots1)
        slots2.sort()
        c1 = 0
        c2 = 0
        n1 = len(slots1)
        n2 = len(slots2)
        while c1 < n1 and c2 < n2:
            if slots1[c1][0] >= slots2[c2][1]:
                c2 += 1
                continue
            if slots1[c1][1] <= slots2[c2][0]:
                c1 += 1
                continue
            if min(slots1[c1][1],slots2[c2][1]) - max(slots1[c1][0],slots2[c2][0]) >= duration:
                return [max(slots1[c1][0],slots2[c2][0]),max(slots1[c1][0],slots2[c2][0]) + duration]
            if slots1[c1][0] < slots2[c2][0]:
                c1 += 1
            elif slots1[c1][0] > slots2[c2][0]:
                c2 += 1
            else:
                if slots1[c1][1] < slots2[c2][1]:
                    c1 += 1
                elif slots1[c1][1] > slots2[c2][1]:
                    c2 += 1
                else:
                    c1 += 1
                    c2 += 1
                
        return []
        