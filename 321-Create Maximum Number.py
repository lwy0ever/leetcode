class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        # 遍历所有从nums1里挑出i个数与nums2里挑出k-i个数的组合方案并取最大值
        # 子问题1:从num里取出相对顺序不变的k个数构成的最大数
        # 子问题2:合并两个数组也需满足两个数组元素的相对顺序不变的最大数
        def pick(num,k):    # 子问题1
            if not k:
                return []
            ans = [10]
            length = len(num)
            cnt = length - k # 可以被移除的数量
            ind = 0
            while ind < length:
                n = num[ind]
                ind += 1
                while cnt > 0 and ans[-1] < n:
                    ans.pop()
                    cnt -= 1
                ans.append(n)
            return ans[1:k + 1]

        def merge(num1,num2):   # 子问题2
            ans = []
            while num1 and num2:
                if num1 > num2:
                    ans.append(num1.pop(0))
                else:
                    ans.append(num2.pop(0))
            ans += num1
            ans += num2
            return ans
        
        ans = []
        for i in range(max(0,k - len(nums2)),min(k + 1,len(nums1) + 1)):
            n1 = pick(nums1,i)
            n2 = pick(nums2,k - i)
            #print(i,n1,n2)
            m = merge(n1,n2)
            #print(m)
            ans = max(ans,m)
        return ans