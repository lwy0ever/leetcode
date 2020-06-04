class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # 反转类似于冒泡,所以只要数组排序后相同,就可以
        target.sort()
        arr.sort()
        return target == arr