class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = 0
        qs = set()
        for qx,qy in queens:
            qs.add((qx,qy))
        di = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        ans = []
        for dx,dy in di:
            step = 1
            while True:
                if king[0] + dx * step >= 0 and king[1] + dy * step >= 0 and king[0] + dx * step < 8 and king[1] + dy * step < 8:
                    if (king[0] + dx * step,king[1] + dy * step) in qs:
                        ans.append([king[0] + dx * step,king[1] + dy * step])
                        break
                else:
                    break
                step += 1
        return ans