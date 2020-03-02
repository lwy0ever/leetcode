class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # 128 = 0b10000000
        # 192 = 0b11000000
        # 224 = 0b11100000
        # 240 = 0b11110000
        
        def cal(d):
            cnt = 0
            while d & 128:
                d <<= 1
                cnt += 1
            return cnt

        n = len(data)
        i = 0
        while i < n:
            ones = cal(data[i])
            #print(ones,bin(data[i]))
            if ones == 0:
                i += 1
                continue
            if 1 < ones <= 4 and i + ones <= n:
                for j in range(i + 1,i + ones):
                    if cal(data[j]) != 1:
                        return False
                i += ones
            else:
                return False
        return True