class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # 假设某个字符串string,len(string)=maxSize
        # 那么string[:minSize]出现的次数一定大于等于string出现的次数,所以maxSize没有用
        # 只需要关注长度=minSize的字符串即可
        n = len(s)
        cnt = collections.Counter() # 字符串出现的次数
        char = collections.Counter()    # 字母出现的次数
        letterNum = 0   # 字母的个数
        for i in range(n):
            if char[s[i]] == 0:
                letterNum += 1
            char[s[i]] += 1
            if i >= minSize:
                char[s[i - minSize]] -= 1
                if char[s[i - minSize]] == 0:
                    letterNum -= 1
            if letterNum <= maxLetters and i - minSize + 1 >= 0:
                cnt[s[i - minSize + 1:i + 1]] += 1
            #print(cnt,char,letterNum)
        #print(cnt)
        return cnt.most_common(1)[0][1] if cnt else 0