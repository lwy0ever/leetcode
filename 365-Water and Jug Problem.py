class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        # 裴蜀定理可以证明：
        # 如果所需要的水量是两个水壶容量的最大公约数的倍数，且水量不大于两个水壶的容量之和，那么必然可以用这两个水壶操作得到所需要的水量
        if x == 0:
            return z in [0,y]
        if y == 0:
            return z in [0,x]
        def lcd(x,y):
            d,m = divmod(x,y)
            if m == 0:
                return y
            return lcd(y,m)
        
        if x + y >= z and z % lcd(x,y) == 0:
            return True
        return False