class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        a = [[] for _ in range(11)]
        a[0] = [0]
        a[1] = [1,2,3,4,5,6,7,8,9]
        for i in range(2,11):
            for x in a[i - 1]:
                if x % 10 > 0:
                    a[i].append(x * 10 + (x % 10 - 1))
                if x % 10 < 9:
                    a[i].append(x * 10 + (x % 10 + 1))
        #print(a)
        ans = []
        for ax in a:
            for x in ax:
                if x >= low:
                    if x <= high:
                        ans.append(x)
                    else:
                        break
        return ans