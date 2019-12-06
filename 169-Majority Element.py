class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 普通方法
        '''
        cnt = collections.Counter(nums)
        return cnt.most_common(1)[0][0]
        '''

        # 投票法Boyer-Moore
        # 本质上， Boyer-Moore 算法就是找 nums 的一个后缀 suf，其中 suf[0] 就是后缀中的众数。我们维护一个计数器，如果遇到一个我们目前的候选众数，就将计数器加一，否则减一。只要计数器等于 0 ，我们就将 nums 中之前访问的数字全部 忘记 ，并把下一个数字当做候选的众数。
        # 翻译一下:
        # 假设i是众数,计数器+1
        # 如果i + 1等于i,则计数器+1,否则计数器-1
        # 计数器为0,则选择下一个作为众数
        # 结果:
        # 如果选择的众数是对的,那么最终计数器会>=0
        # 如果选择的众数是错的,那么会有一些真正的众数和非真正的众数被中和为0,其中真正的众数数量不会超过一半
        ans = 0
        cnt = 0
        for n in nums:
            if cnt == 0:
                ans = n
                cnt = 0
            if ans == n:
                cnt += 1
            else:
                cnt -= 1
        return ans