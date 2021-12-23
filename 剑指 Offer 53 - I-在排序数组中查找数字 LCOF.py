class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 二分查找
        return bisect.bisect_right(nums,target) - bisect.bisect_left(nums,target)