class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # 有重复的旋转排序数组,使用二分查找,速度提升有限,跳过此题
        for n in nums:
            if n == target:
                return True
        return False