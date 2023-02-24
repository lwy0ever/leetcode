class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # 最后一定是所有students是同一类,然后卡死
        cnt = collections.Counter(students)
        for s in sandwiches:
            if cnt[s] > 0:
                cnt[s] -= 1
            else:
                return cnt[1 ^ s]
        return 0