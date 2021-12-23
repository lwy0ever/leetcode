class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # 不需要模拟,只需要知道0和1的学生数量
        # 学生可以循环排队,sandwich不能
        # 所以循环sandwich,检查是否有学生爱吃
        n = len(students)
        s1 = sum(students)
        s0 = n - s1
        for sw in sandwiches:
            if sw == 0:
                if s0 > 0:
                    s0 -= 1
                else:
                    break
            else:   # sw == 1
                if s1 > 0:
                    s1 -= 1
                else:
                    break
        return s0 + s1