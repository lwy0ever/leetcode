class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        # DP
        n = len(nums1)
        swap = 1    #表示i-1位发生交换的情况下,最小交换次数
        noswap = 0    #表示i-1位没发生交换的情况下,最小交换次数
        for i in range(1,n):
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]: #本来不用换
                if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]: #换了也满足
                    swap = min(swap,noswap) + 1   #那么i次换就是i-1次的小值加1次
                    noswap = swap - 1
                else:   #换了不满足,所以本来第i位不能换
                    # 但是如果i-1位换了,则i位需要交换
                    swap += 1
            else:   #本来需要换
                # 如果i-1换了,则i位不用换-->noswap = swap
                # 如果i-1没换,则i位换-->swap = noswap + 1
                noswap,swap = swap,noswap + 1
        return min(swap,noswap)