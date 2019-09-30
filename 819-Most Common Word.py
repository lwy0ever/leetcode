class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        para = paragraph.lower()
        cnt = collections.Counter(re.findall(r'[a-z]+',para))
        #print(cnt)
        for b in banned:
            if b in cnt:
                del cnt[b]
        return cnt.most_common(1)[0][0]