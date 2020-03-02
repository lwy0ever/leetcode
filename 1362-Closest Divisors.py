class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        a = 1
        b = num + 2
        for i in range(int((num + 2) ** 0.5),0,-1):
            if (num + 2) % i == 0:
                if (num + 2) // i - i < b - a:
                    b = (num + 2) // i
                    a = i
                    break
        for i in range(int((num + 1) ** 0.5),0,-1):
            if (num + 1) % i == 0:
                if (num + 1) // i - i < b - a:
                    b = (num + 1) // i
                    a = i
                    break
        return [a,b]