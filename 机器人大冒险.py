class Solution:
    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:
        track = []
        px = py = 0
        for c in command:
            if c == 'U':
                py += 1
            else:
                px += 1
            track.append((px,py))
        canReach = False
        for tx,ty in track:
            if (x - tx) * py == (y - ty) * px:
                canReach = True
                break
        if not canReach:
            return False
        for o in obstacles:
            if o[0] <= x and o[1] <= y:
                for tx,ty in track:
                    if (o[0] - tx) * py == (o[1] - ty) * px:
                        return False
        return True
                