class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # 找规律
        # 将下一行的数字>>1,然后对除第1位外取补,就是它的上一行路径
        n = len(bin(label)) - 2 - 1
        firstBit = 2 ** n
        mask = 2 ** n - 1
        ans = []
        while label:
            ans.append(label)
            firstBit >>= 1
            label = (label >> 1) ^ firstBit ^ mask
            mask >>= 1
        return ans[::-1]