class Solution:

    import random
    def __init__(self, nums: List[int]):
        self.d = collections.defaultdict(list)
        for i,n in enumerate(nums):
            self.d[n].append(i)
        

    def pick(self, target: int) -> int:
        return random.choice(self.d[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)