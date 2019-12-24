class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = 0
        for n in nums:
            s ^= n
        # s为num的异或和
        # 由于有2个不同的number出现1次,这两个number的异或一定不为0,且等于s
        # 利用s的任意一位1,将nums分为2部分,则2个number分别位于这2部分,这里用s & (-s)取最低位
        lowest = s & (-s)
        ans = [0,0]
        for n in nums:
            if n & lowest == 0:
                ans[0] ^= n
            else:
                ans[1] ^= n
        return ans