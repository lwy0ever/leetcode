class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 整数的数组nums中的数字范围是[1,n]
        # 考虑以下两种情况:
        # 1,如果数组中没有重复的数,则下标i和nums[i]会有一一对应的关系,nums[i]->nums[nums[i]]->...会形成一个类似链表的结构
        # 2,如果数组中有重复的数,会存在nums[i] == nums[j],于是会出现循环,而且是多对1的关系
        # 算法:
        # 1,利用快慢指针找到循环的入口
        # 2,利用142题(https://leetcode-cn.com/problems/linked-list-cycle-ii/)的证明,两个指针分别从相遇点和起点开始移动,会在循环入口处相遇,循环入口即为重复数字
        slow = 0
        fast = 0
        slow = nums[slow]
        fast = nums[nums[fast]]
        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]
        p1 = 0
        p2 = slow
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
        return p1