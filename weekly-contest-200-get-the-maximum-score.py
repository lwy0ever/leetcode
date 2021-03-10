class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        dp1 = [0] * (n1 + 1)
        dp2 = [0] * (n2 + 1)
        ind1 = 0
        ind2 = 0
        while ind1 < n1 and ind2 < n2:
            if nums1[ind1] == nums2[ind2]:
                dp1[ind1 + 1] = max(dp1[ind1],dp2[ind2]) + nums1[ind1]
                dp2[ind2 + 1] = dp1[ind1 + 1]
                ind1 += 1
                ind2 += 1
            elif nums1[ind1] > nums2[ind2]:
                dp2[ind2 + 1] = dp2[ind2] + nums2[ind2]
                ind2 += 1
            else:   # nums1[ind1] < nums2[ind2]
                dp1[ind1 + 1] = dp1[ind1] + nums1[ind1]
                ind1 += 1
        while ind1 < n1:
            dp1[ind1 + 1] = dp1[ind1] + nums1[ind1]
            ind1 += 1
        while ind2 < n2:
            dp2[ind2 + 1] = dp2[ind2] + nums2[ind2]
            ind2 += 1
        #print(dp1)
        #print(dp2)
        return max(dp1[-1],dp2[-1]) % (10 ** 9 + 7)
