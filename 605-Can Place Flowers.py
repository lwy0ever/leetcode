class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        pre = 0
        l = len(flowerbed)
        i = 0
        while i < l:
            f = flowerbed[i]
            if f:
                if i + 2 < l:   # f = 1,跳2格
                    i += 1
                    pre = flowerbed[i]
                else:
                    break
            else:
                if pre == 1:
                    pre = 0
                else:   # pre = 0,f = 0
                    if i + 1 < l:
                        if flowerbed[i + 1]:    # after = 1,跳2格(其实可以跳3格,但是判断有点太复杂了)
                            i += 1
                            pre = 1
                        else:
                            n -= 1
                            pre = 1
                            if n == 0:
                                return True
                    else:   # i + 1 = l,末尾情况
                        if n == 1:
                            return True
            i += 1
        return False