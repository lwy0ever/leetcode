class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # 将二进制数相同的元素存放在一起,记录最长的单词长度
        numLongestWord = collections.defaultdict(int)
        for w in words:
            num = 0
            for c in w:
                num |= 1 << (ord(c) - ord('a'))
            numLongestWord[num] = max(numLongestWord[num],len(w))
        #print(nums)
        ans = 0
        for i in numLongestWord.keys():
            for j in numLongestWord.keys():
                if i & j == 0:
                    ans = max(ans,numLongestWord[i] * numLongestWord[j])
        return ans