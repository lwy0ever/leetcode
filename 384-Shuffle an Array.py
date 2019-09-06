import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        array = list(self.nums)
        n = len(array)
        for i in range(n):
            j = random.randrange(n)
            array[i],array[j] = array[j],array[i]
        return array
        '''
        array = list(self.nums)
        random.shuffle(array)
        return array
        '''


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()