class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for i in points:
            distance_num = collections.defaultdict(int)   # distance_num[d]存储距离点i的距离为d ** 0.5的点的数量
            for j in points:
                if i != j:
                    distance_num[(i[0] - j[0]) * (i[0] - j[0]) + (i[1] - j[1]) * (i[1] - j[1])] += 1
            for n in distance_num.values():
                # 有n个等距离的点,从中任选2个即为1组解,所以有n * (n - 1)组解
                # 这里是n * (n - 1),而不是n * (n - 1) // 2,因为"需要考虑元组的顺序",(i,j,k)和(i,k,j)是2组不同的解
                ans += n * (n - 1)
            #print(distance_num)
        return ans