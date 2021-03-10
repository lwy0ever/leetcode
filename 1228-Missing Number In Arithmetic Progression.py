class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        d = []
        d.append(arr[1] - arr[0])
        if d[0] == 0:
            return 0
        d.append(arr[0])
        d.append(1)
        pre = arr[1]
        for a in arr[2:]:
            if a - pre == d[0]:
                if len(d) > 3:
                    return d[4] + d[0]
                else:
                    d[2] += 1
            else:
                if len(d) > 3:
                    return d[1] + d[3]
                else:
                    d.append(a - pre)
                    d.append(pre)
                    d.append(1)
            pre = a
            #print(d)
        if abs(d[0]) > abs(d[3]):
            return d[1] + d[3]
        else:
            return d[4] + d[0]
