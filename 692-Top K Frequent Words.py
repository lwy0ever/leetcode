class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = collections.Counter(words)
        ans = sorted(cnt.keys(),key = lambda x:(-cnt[x],x))
        return ans[:k]