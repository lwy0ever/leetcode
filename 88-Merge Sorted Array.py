class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 由于nums1尾部是空白的,可以从后向前检查nums1[:m]和nums2,从后向前填充nums1
        cur1 = m - 1
        cur2 = n - 1
        pos = m + n - 1
        while cur1 >= 0 and cur2 >= 0:
            # 把大数放在尾部,并且将贡献大数的指针前移
            if nums1[cur1] <= nums2[cur2]:
                nums1[pos] = nums2[cur2]
                cur2 -= 1
            else:
                nums1[pos] = nums1[cur1]
                cur1 -= 1
            pos -= 1
        # 如果cur2 >= 0,说明nums2还有没有被处理过的元素,填充到nums1的头部
        nums1[:cur2 + 1] = nums2[:cur2 + 1]