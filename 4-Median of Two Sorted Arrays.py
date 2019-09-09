class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            n1,n2 = n2,n1
            nums1,nums2 = nums2,nums1
        
        # nums1中的i-1,i分属两个区间
        # nums2中的j-1,j分属两个区间
        # 左区间等于右区间大小 or 左区间 = 右区间 + 1
        imin, imax, half_len = 0, n1, (n1 + n2 + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < n1 and nums2[j - 1] > nums1[i]:
                # i is too small, find it in the right half
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # i is too big, find it in the left half
                imax = i - 1
            else:
                # i is perfect
                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])

                if (n1 + n2) % 2 == 1:
                    return max_of_left

                if i == n1: min_of_right = nums2[j]
                elif j == n2: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2
