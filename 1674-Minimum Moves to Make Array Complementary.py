class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        # 定义nums[i]为A,nums[n - 1 - i]为B:
        # 则互补之后,A + B在[2,limit * 2]的范围
        
        # 我们对[2,limit * 2]范围内的每种情况进行尝试:
        # 可以将[2,limit * 2]划分为3个区间:
        # 区间1:[2,1 + min(A,B)),需要2次操作
        # 区间2:[1 + min(A,B),limit + max(A,B)],需要1次操作(其中A + B需要0次)
        # 区间3:(limit + max(A,B),limit * 2],需要2次操作
        
        # 如果对[2,limit * 2]里面每个数字都做更新,则操作复杂度较高
        # 由于区间连续,可以使用差分数组
        n = len(nums)
        operation = [0] * (limit * 2 + 2)   # operation[i]表示以i为A + B的目标,所需要的操作次数的差分数组,由于是差分数组,i的有效范围从2到limit * 2 + 1
        # 区间初始化为1和3
        operation[2] += n
        operation[limit * 2 + 1] -= n
        #print(operation)
        for i in range(n // 2):
            A = nums[i]
            B = nums[n - 1 - i]
            # 区间2里的数字,操作次数-1
            operation[1 + min(A,B)] -= 1
            operation[limit + max(A,B) + 1] += 1
            # 如果刚好是A + B,则操作次数再-1
            operation[A + B] -= 1
            operation[A + B + 1] += 1
            #print(operation)
        ans = n # 初始化为最大值
        s = 0
        for i in range(2,limit * 2 + 1):
            s += operation[i]
            ans = min(ans,s)
        return ans