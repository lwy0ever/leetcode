class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # 只要两者包含的字符种类相同,并且字符出现的次数相同,则可以通过操作2将两者字符变成一样的
        # 然后再通过操作1调整顺序
        cnt1 = collections.Counter(word1)
        cnt2 = collections.Counter(word2)
        return sorted(cnt1.keys()) == sorted(cnt2.keys()) and sorted(cnt1.values()) == sorted(cnt2.values())