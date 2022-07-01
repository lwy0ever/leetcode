class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # 条件3:age[y] > 100 and age[x] < 100,是条件2的子集,可以忽略
        # age[x] * 0.5 + 7 <= age[y] < age[x],则x向y发送请求
        # 当age[x] * 0.5 + 7 >= age[x]也就是age <= 14,必然不满足
        
        # 方法1:排序 + 双指针
        '''
        n = len(ages)
        ages.sort()
        left = 0    # 表示age[x] * 0.5 + 7 < age[y]的x的数量
        right = 0   # 表示age[x] > age[y]的数量
        ans = 0
        for age in ages:    # age就是age[y]
            if age <= 14:
                continue
            while ages[left] <= 0.5 * age + 7:
                left += 1
            while right + 1 < n and ages[right + 1] <= age:
                right += 1
            ans += right - left
        return ans
        '''

        # 方法2:由于年龄范围在1-120之间,考虑使用计数排序代替普通的排序
        # 为了方便计数排序求和,使用前缀和
        cnt = [0] * 121
        for age in ages:
            cnt[age] += 1
        pre = [0] * 121
        for i in range(1,121):
            pre[i] = pre[i - 1] + cnt[i]

        ans = 0
        for i in range(15,121):
            if cnt[i] > 0:
                bound = int(i * 0.5 + 7)
                ans += cnt[i] * (pre[i] - pre[bound] - 1)
        return ans
