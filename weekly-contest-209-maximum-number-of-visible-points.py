class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        # 先计算每个points到location形成的直线 和 location水平直线 形成的角度
        # 以向右为0度
        # 右上角为0-90度,特点:pointsY >= locationY,pointsX >= locationX,取arctan(ΔY/ΔX)
        # 左上角为90-180度,特点:pointsY >= locationY,pointsX <= locationX,取180 - arctan(ΔY/-ΔX)
        # 左下角为180-270度,特点:pointsY <= locationY,pointsX <= locationX,取180 + arctan(ΔY/ΔX)
        # 左下角为270-360度,特点:pointsY <= locationY,pointsX >= locationX,取360 - arctan(-ΔY/ΔX)
        base = 0    # 记录和location重合的点
        lx,ly = location
        angles = []
        for x,y in points:
            if lx == x and ly == y:
                base += 1
                continue
            dy = y - ly
            dx = x - lx
            if dx == 0:
                if dy > 0:
                    a = 90
                else:
                    a = 270
            else:
                if dx > 0 and dy >= 0:
                    a = math.degrees(atan(dy / dx))
                elif dx < 0 and dy >= 0:
                    a = 180 - math.degrees(atan(-dy / dx))
                elif dx < 0 and dy <= 0:
                    a = 180 + math.degrees(atan(dy / dx))
                else:
                    a = 360 - math.degrees(atan(-dy / dx))
            angles.append(a)
        n = len(angles)
        #print(n)
        angles.sort()
        #print(angles)
        ans = 0
        left = 0
        right = 0
        while left < n:
            if left == right:
                right = (left + 1) % n
            while (angles[right] + 360 - angles[left]) % 360 <= angle:
                right = (right + 1) % n
                if right == left:   # 套圈了,全都满足
                    #print(left,right,base,n)
                    return base + n
            #print(left,right)
            ans = max(ans,(right + n - left) % n)
            left += 1
        return base + ans