class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 思路一样,简化写法
        five = 0    # 表示5美元的钞票数量
        ten = 0 # 表示10美元的钞票数量
        for b in bills:
            if b == 20:
                ten -= 1
                five -= 1
            elif b == 10:
                five -= 1
                ten += 1
            else:   # b == 5
                five += 1
            if ten < 0:
                five -= 2
                ten += 1
            if ten < 0 or five < 0:
                return False
        return True

        '''
        five = 0    # 表示5美元的钞票数量
        ten = 0 # 表示10美元的钞票数量
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False
            else:   # b == 20
                # 优先用大数找零
                if ten > 0:
                    if five > 0:
                        five -= 1
                        ten -= 1
                    else:
                        return False
                else:
                    if five >= 3:
                        five -= 3
                    else:
                        return False
        return True
        '''