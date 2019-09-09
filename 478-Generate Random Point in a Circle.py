class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        # 以下注释不太懂
        # 极坐标变换
        # dS = dxdy = rdrdθ = d(r^2)dθ/2, 在0 ~ r^2上才是均匀分布
        radius = random.random() ** 0.5 * self.r
        angel = random.random() * 2 * math.pi
        x = self.x + radius * math.cos(angel)
        y = self.y + radius * math.sin(angel)
        return [x,y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()