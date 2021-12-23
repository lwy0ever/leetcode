class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 排序+双指针
        # 因为每船最多2人
        # 如果体重最重的可以和最轻的合乘,一定是最大化利用了重量
        # 否则就是体重最重的人单独乘坐
        ans = 0
        n = len(people)
        people.sort()
        l = 0
        r = n - 1
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
            ans += 1
        return ans