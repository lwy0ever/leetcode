class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        # 纯数组运算
        s1 = set(nums1)
        s2 = set(nums2)
        s3 = set(nums3)
        return list((s1 & s2) | (s2 & s3) | (s1 & s3))
        
        '''
        # 数组 + hash
        s1 = set(nums1)
        s2 = set(nums2)
        s3 = set(nums3)
        ans = []
        for n in s1 | s2 | s3:
            if (n in s1) + (n in s2) + (n in s3) >= 2:
                ans.append(n)
        return ans
        '''