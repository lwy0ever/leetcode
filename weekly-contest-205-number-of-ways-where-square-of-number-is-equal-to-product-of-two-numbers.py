class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        n1 = len(nums1)
        n2 = len(nums2)
        # nums1[i]2 == nums2[j] * nums2[k]
        cachePower2 = {}    # 表示2次方结果出现的次数
        cacheMul = {}   # 表示乘积结果出现的次数
        for i in range(n1):
            cachePower2[nums1[i] * nums1[i]] = cachePower2.get(nums1[i] * nums1[i],0) + 1
        for j in range(n2 - 1):
            for k in range(j + 1,n2):
                cacheMul[nums2[j] * nums2[k]] = cacheMul.get(nums2[j] * nums2[k],0) + 1
        for p2 in cachePower2.keys():
            if p2 in cacheMul:
                ans += cachePower2[p2] * cacheMul[p2]
        # nums2[i]2 == nums1[j] * nums1[k]
        cachePower2 = {}    # 表示2次方结果出现的次数
        cacheMul = {}   # 表示乘积结果出现的次数
        for i in range(n2):
            cachePower2[nums2[i] * nums2[i]] = cachePower2.get(nums2[i] * nums2[i],0) + 1
        for j in range(n1 - 1):
            for k in range(j + 1,n1):
                cacheMul[nums1[j] * nums1[k]] = cacheMul.get(nums1[j] * nums1[k],0) + 1
        for p2 in cachePower2.keys():
            if p2 in cacheMul:
                ans += cachePower2[p2] * cacheMul[p2]
        return ans