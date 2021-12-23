class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 投票算法
        vote = 0
        cnt = 0
        for n in nums:
            if cnt == 0:
                vote = n
            if vote == n:
                cnt += 1
            else:
                cnt -= 1
        # 检查是否过半
        cnt = 0
        for n in nums:
            if n == vote:
                cnt += 1
        return vote if cnt * 2 > len(nums) else -1