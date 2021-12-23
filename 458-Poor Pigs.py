class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # 每只小猪可以给出信息量minutesToTest // minutesToDie + 1
        return int(math.ceil(math.log(buckets,minutesToTest // minutesToDie + 1)))    