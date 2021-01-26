class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        # 从前向后将数字压入stack,最后k - len(stack)直接压入
        # 如果nums[i] < stack[-1],则弹出,并继续比较(同时需要注意nums剩余的长度是否足够长)
        n = len(nums)
        stack = []
        i = 0
        cnt = 0
        while i < n:
            while cnt and nums[i] < stack[-1] and n - i + cnt > k:
                stack.pop()
                cnt -= 1
            #print(stack)
            if cnt < k:
                stack.append(nums[i])
                cnt += 1
            #print(stack)
            i += 1
        stack += nums[i:]
        return stack