class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # 先用正则分组
        r1 = re.findall(r'(-?\d+)\+(-?\d+)i',num1)[0]
        r2 = re.findall(r'(-?\d+)\+(-?\d+)i',num2)[0]
        #print(r1,r2)
        a = int(r1[0]) * int(r2[0]) - int(r1[1]) * int(r2[1])
        b = int(r1[0]) * int(r2[1]) + int(r1[1]) * int(r2[0])
        return f'{a}+{b}i'