class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums


    def reset(self) -> List[int]:
        return self.nums


    def shuffle(self) -> List[int]:
        array = list(self.nums)
        n = len(array)
        for i in range(n):
            j = random.randrange(n)
            array[i],array[j] = array[j],array[i]
        return array



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()