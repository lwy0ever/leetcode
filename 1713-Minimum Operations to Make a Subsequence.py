class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        # len(target) = m,len(arr) = n
        # 类似求最长公共子序列:题目1143,O(mn)
        # 由于target各元素不同,用pos记录target[i]的位置
        # 于是target = [pos[0],pos[1],pos[2],...]
        # 统计arr[i]在target中出现的位置(没有出现的可以忽略),记录为stack
        # 找arr的最长递增子序列:题目300
        # 数字对应坐标
        pos = {v:i for i,v in enumerate(target)}
        stack = []
        for v in arr:
            if v in pos:
                p = pos[v]
                i = bisect.bisect_left(stack,p)
                if i == len(stack):
                    stack.append(0)
                stack[i] = p
        return len(target) - len(stack)