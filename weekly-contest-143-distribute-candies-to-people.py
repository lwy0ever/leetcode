class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # 第1循环,从1到n,需要(1 + n) * n / 2个candies
        # 第2循环,从n + 1到n + n,需要(n * 3 + 1) * n / 2个candies,比第1个循环多了n * n个
        # 经过x轮循环以后,第1个人有1 * x + n * (x - 1)个,第2个人有2 * x + n * (x - 1)个...
        # 如果不够整轮了,则摆放第1个人1 + n * x个,第2个人2 + n * x个...
        if num_people == 1:
            return [candies]
        circle = 0
        needed = (1 + num_people) * num_people // 2
        while candies >= needed:
            #print(circle,candies,needed)
            circle += 1
            candies -= needed
            needed += num_people * num_people
        ans = []
        for i in range(num_people):
            ans.append((i + 1) * circle + num_people * (circle - 1) * circle // 2)
        #print(circle,ans,candies)
        for i in range(num_people):
            if candies >= i + 1 + num_people * circle:
                ans[i] += i + 1 + num_people * circle
                candies -= i + 1 + num_people * circle
            else:
                ans[i] += candies
                break
        return ans