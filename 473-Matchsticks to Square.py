class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        # 这个算法比较快
        n = len(nums)
        if n < 4: return False
        s = sum(nums)
        if s % 4 > 0: return False
        length = s // 4
        if max(nums) > length: return False
        nums.sort(reverse = True)  # 先考虑大数,方便剪枝
        
        def t(needed,added,mask):   # 表示还需要找到needed个边,当前边已知和为added,火柴使用情况为mask
            #print(needed,added,bin(mask))
            if needed == 0:
                return True
            if added == length:
                return t(needed - 1,0,mask)
            if added == 0:  # 空边,先放一个进去
                for i in range(n):
                    if mask & (1 << i) == 0:
                        return t(needed,nums[i],mask | (1 << i))
            for i in range(n):
                # 没有使用nums[i],并且可以使用
                if mask & (1 << i) == 0:
                    if added + nums[i] <= length:
                        if t(needed,added + nums[i],mask | (1 << i)):
                            return True
            return False
        return t(3,0,0)

        '''
        # O(4 ** N)
        n = len(nums)
        if n < 4:
            return False
        s = sum(nums)
        if s % 4 > 0:
            return False
        length = s // 4
        nums.sort(reverse = True)  # 先考虑大数,方便剪枝

        def t(arr,ind): # arr[0:4]表示4个边已有的长度,ind表示当前需要考虑nums[ind]
            if ind == n:    # 都放完了,说明肯定满足了
                return True
            #print(arr,ind)
            for i in range(4):
                if arr[i] + nums[ind] <= length:
                    tArr = arr.copy()
                    tArr[i] += nums[ind]
                    if t(tArr,ind + 1):
                        return True
            return False
        
        return t([0] * 4,0)
        '''