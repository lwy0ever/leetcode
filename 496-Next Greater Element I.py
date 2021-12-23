class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 单调栈 + 哈希
        res = dict()    # res[i]表示数字i的下一个更大元素
        stack = []
        for n in nums2[::-1]:
            while stack and stack[-1] < n:
                stack.pop()
            if stack:
                res[n] = stack[-1]
            else:
                res[n] = -1
            stack.append(n)
        return [res[n] for n in nums1]