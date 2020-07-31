class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        # 快慢指针
        n = len(nums)
        nxt = lambda x:(x + nums[x]) % n
        
        for i in range(n):
            slow = i
            fast = nxt(i)   # 因为要判断slow == fast,所以错开一步
            # 同方向
            while nums[slow] * nums[nxt(slow)] > 0 and nums[fast] * nums[nxt(nxt(fast))] > 0:
                if slow == fast:    # 追上了
                    if slow == nxt(slow):   # 循环长度为1
                        break
                    else:
                        return True
                slow = nxt(slow)
                fast = nxt(nxt(fast))
            v = nums[i]
            # 已经尝试过的,置0
            while nums[i] * v > 0:
                t = i
                i = nxt(i)
                nums[t] = 0
        return False