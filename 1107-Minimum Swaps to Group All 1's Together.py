class Solution:
    def minSwaps(self, data: List[int]) -> int:
        n = len(data)
        ones = data.count(1)
        cur = data[:ones].count(0)
        mi = cur
        for i in range(ones,n):
            if data[i] != data[i - ones]:
                if data[i] == 1:
                    cur -= 1
                    mi = min(mi,cur)
                else:
                    cur += 1
        return mi
        