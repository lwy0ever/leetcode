class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for w in range(int(math.sqrt(area)),0,-1):
            if area % w == 0:
                return [area // w,w]