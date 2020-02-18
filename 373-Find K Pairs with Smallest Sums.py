class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 == 0 or n2 == 0:
            return ans
        cur = [0] * n1  # cur[i]表示nums1取第i个数的时候,nums2取到的第几个数字
        stack = []  # 记录最小值的可能组合
        _sum = []   # 记录组合的值
        n1Index = []    # 记录stack[i]中nums1的位置
        for i in range(n1):
            stack.append([nums1[i],nums2[0]])
            _sum.append(nums1[i] + nums2[0])
            n1Index.append(i)
        #print('init:',_sum,stack,n1Index,cur)

        while len(ans) < k:
            if stack:
                s = stack.pop(0)
                ind = n1Index.pop(0)
                _sum.pop(0)
                ans.append(s)
            else:
                break
            cur[ind] += 1
            if cur[ind] < n2:
                pos = bisect.bisect(_sum,nums1[ind] + nums2[cur[ind]])
                stack.insert(pos,[nums1[ind],nums2[cur[ind]]])
                _sum.insert(pos,nums1[ind] + nums2[cur[ind]])
                n1Index.insert(pos,ind)
            #print(_sum,stack,n1Index,cur)
        return ans