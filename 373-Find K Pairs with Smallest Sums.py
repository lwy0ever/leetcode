class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # 方法1:官方解法1
        m, n = len(nums1), len(nums2)
        ans = []
        # 考虑nums1[0]和nums2[i]的组合
        pq = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, m))]
        while pq and len(ans) < k:
            _, i, j = heappop(pq)
            ans.append([nums1[i], nums2[j]])
            # 如果nums1[i],nums2[j]是最新的最小值
            # 则需要将(nums1[i + 1],nums2[j])和(nums1[i],nums2[j + 1])纳入考虑
            # 为了避免重复,已经将(nums1[i + 1],nums2[j])纳入考虑
            if j + 1 < n:
                heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans


        # 方法2:
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