class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 高个子先站好位，矮个子插入到K位置上，前面肯定有K个高个子，矮个子再插到前面也满足K的要求
        people.sort(key = lambda p:(-p[0],p[1]))
        ans = []
        for p in people:
            ans.insert(p[1],p)
        return ans
        '''
        n = len(people)
        ans = [None] * n
        people.sort(key = lambda p:(p[0],p[1]))
        #print(people)
        for i in range(n):
            p = people[i]
            cnt = 0
            for j in range(n):
                if not ans[j] or ans[j][0] >= p[0]:
                    if cnt == p[1]:
                        ans[j] = p
                        break
                    cnt += 1
        return ans
        '''