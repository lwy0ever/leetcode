class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 二分查找
        n = len(citations)
        left = 0
        right = n - 1
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            # 至少有h篇论文被引用了至少h次
            # 数组长度为n
            # 有n - i篇论文至少被引用了citations[i]次
            # 若citations[i]满足要求,则citations[i] >= n-i
            if citations[mid] >= n - mid:
                ans = n - mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
