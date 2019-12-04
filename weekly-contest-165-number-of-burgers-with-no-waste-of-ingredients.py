class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        t = tomatoSlices - cheeseSlices * 2
        if t % 2 == 0 and 0 <= t // 2 <= cheeseSlices:
            return [t // 2,cheeseSlices - t // 2]
        return []