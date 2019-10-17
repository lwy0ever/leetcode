class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            cnt = [0] * 26
            for c in s:
                cnt[ord(c) - ord('a')] += 1
            ans[tuple(cnt)].append(s)
        return ans.values()

        '''
        ans = []
        cnts = []
        for s in strs:
            cnt = collections.Counter(s)
            if cnt in cnts:
                p = cnts.index(cnt)
                ans[p].append(s)
            else:
                cnts.append(cnt)
                ans.append([s])
        return ans
        '''