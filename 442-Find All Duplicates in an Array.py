class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # 由于1 <= nums[i] <= n
        # 逐个位置检查,nums[i]应该放到位置nums[i] - 1
        # 1,如果该位置已经有该数or本身就是自己,则该位置已经放置了正确的数字
        # 2,如果该位置i不是该数i + 1,则将nums[i]和其应该在的位置上的数字nums[nums[i] - 1]交换位置,继续该过程
        ans = []
        n = len(nums)
        for i in range(n):
            #print(i)
            while nums[i] != nums[nums[i] - 1]:
                # nums[i]要后赋值,否则nums[nums[i] - 1]就错了
                # 也就是,不能写成nums[i],nums[nums[i] - 1] = nums[nums[i] - 1],nums[i]
                nums[nums[i] - 1],nums[i] = nums[i],nums[nums[i] - 1]
                #print(nums)
        for i,a in enumerate(nums,1):
            if i != a:
                ans.append(a)
        return ans