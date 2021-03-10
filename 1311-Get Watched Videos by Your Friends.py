class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        # bfs
        fromP = {id}
        visited = {id}
        l = 0
        while fromP and l < level:
            l += 1
            toP = set()
            for f in fromP:
                for newFriend in friends[f]:
                    if newFriend not in visited:
                        toP.add(newFriend)
                        visited.add(newFriend)
            fromP = toP
        if l < level:
            return []
        #print(fromP)
        cnt = collections.Counter()
        for f in fromP:
            cnt += collections.Counter(watchedVideos[f])
        #print(cnt)
        
        return [k for k,v in sorted(cnt.items(),key = lambda x:(x[1],x[0]))]